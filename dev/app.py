from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_file
import sqlite3
import os
import tensorflow as tf
import numpy as np
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from fpdf import FPDF

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management
UPLOAD_FOLDER = 'uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load CNN Model
model = load_model('dev/diabetic_retinopathy_model.h5')

# Initialize Database
conn = sqlite3.connect('users.db', check_same_thread=False)
c = conn.cursor()

# Create Users Table
c.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    doctor_id TEXT,
    hospital TEXT,
    specialization TEXT,
    username TEXT UNIQUE,
    email TEXT UNIQUE,
    password TEXT
)''')

# Create Patients Table
c.execute('''CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    eye_issue TEXT,
    diabetes TEXT,
    duration TEXT,
    image_path TEXT,
    diagnosed_by TEXT,
    diagnosis_result TEXT, pdf_report_path TEXT
)''')
conn.commit()

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize
    return img_array

def get_static_recommendations(progression_level):
    recommendations = {
        "No DR": {
            "risk_analysis": "No signs of diabetic retinopathy detected.",
            "early_detection_analysis": "The model suggests regular eye check-ups for preventive care.",
            "predictive_analysis": "No signs of disease progression detected.",
            "recommendation": "Routine checkups and healthy lifestyle maintenance.",
            "guidance": "Regular eye exams and controlled blood sugar levels recommended."
        },
        "Mild": {
            "risk_analysis": "Early signs of DR detected, but not severe.",
            "early_detection_analysis": "Early detection is crucial; yearly screenings recommended.",
            "predictive_analysis": "Potential for progression; lifestyle changes recommended.",
            "recommendation": "Yearly screenings and lifestyle adjustments advised.",
            "guidance": "Monitor blood pressure and cholesterol to slow progression."
        },
        "Moderate": {
            "risk_analysis": "Moderate DR detected, requiring closer observation.",
            "early_detection_analysis": "Signs of DR suggest more frequent monitoring.",
            "predictive_analysis": "Progression risk is moderate; intervention may be needed.",
            "recommendation": "Ophthalmologist visits every 6 months recommended.",
            "guidance": "Strict glucose control and possible early intervention required."
        },
        "Severe": {
            "risk_analysis": "High risk of vision impairment due to DR progression.",
            "early_detection_analysis": "Urgent intervention recommended to prevent further damage.",
            "predictive_analysis": "Disease progression is accelerating; treatment needed.",
            "recommendation": "Immediate medical evaluation required.",
            "guidance": "Potential laser treatment or medication intervention needed."
        },
        "Proliferative": {
            "risk_analysis": "Critical stage of DR detected, vision at serious risk.",
            "early_detection_analysis": "Emergency medical attention required to prevent vision loss.",
            "predictive_analysis": "Significant progression detected; urgent action needed.",
            "recommendation": "Urgent specialist treatment necessary.",
            "guidance": "Advanced procedures such as anti-VEGF injections or surgery required."
        }
    }
    return recommendations.get(progression_level, recommendations["No DR"])

def generate_insights(prediction):
    severity_levels = ["No DR", "Mild", "Moderate", "Severe", "Proliferative"]
    if prediction.shape != (5,):
        return {"error": f"Invalid prediction format. Expected (5,), but got {prediction.shape}"}
    max_index = np.argmax(prediction)
    max_confidence = prediction[max_index] * 100
    progression_level = severity_levels[max_index]
    if max_confidence < 50:
        progression_level = "No DR"
    static_recs = get_static_recommendations(progression_level)
    insights = {
        "risk_assessment": (
            f"Severity Level: {progression_level}\n"
            f"Confidence Score: {max_confidence:.2f}%\n"
            f"Analysis: {static_recs['risk_analysis']}"
        ),
        "early_detection": (
            f"Detection Level: {progression_level}\n"
            f"Confidence Score: {max_confidence:.2f}%\n"
            f"Analysis: {static_recs['early_detection_analysis']}"
        ),
        "predictive_analysis": (
            f"Disease Progression: {progression_level}\n"
            f"Confidence Score: {max_confidence:.2f}%\n"
            f"Analysis: {static_recs['predictive_analysis']}"
        ),
        "alerts_followups": (
            f"Follow-up Requirement: {progression_level}\n"
            f"Confidence Score: {max_confidence:.2f}%\n"
            f"Recommendation: {static_recs['recommendation']}"
        ),
        "educational_insights": (
            f"Patient Education Level: {progression_level}\n"
            f"Confidence Score: {max_confidence:.2f}%\n"
            f"Guidance: {static_recs['guidance']}"
        )
    }
    return insights

def generate_pdf(name, age, gender, eye_issue, diabetes, duration, image_path, insights):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Diabetic Retinopathy Diagnosis Report", ln=True, align='C')
    pdf.ln(10)
    
    # Patient Details in Left, Image in Right
    pdf.cell(100, 10, f"Patient Name: {name}", ln=True)
    pdf.cell(100, 10, f"Age: {age}", ln=True)
    pdf.cell(100, 10, f"Gender: {gender}", ln=True)
    pdf.cell(100, 10, f"Previous Eye Issues: {eye_issue}", ln=True)
    pdf.cell(100, 10, f"Diabetes: {diabetes}", ln=True)
    pdf.cell(100, 10, f"Diabetes Duration: {duration} years", ln=True)
    pdf.image(image_path, x=140, y=30, w=50)
    pdf.ln(60)
    pdf.cell(0, 10, "____________________________________________________", ln=True, align='C')
    pdf.ln(3)
    
    # AI-Generated Insights
    for key, value in insights.items():
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(0, 10, f"{key.replace('_', ' ').title()}:", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, f"{value}\n")
        pdf.ln(5)
    
    pdf_path = f"uploads/{name}_diagnosis_report.pdf"
    pdf.output(pdf_path)
    return pdf_path


# Home (Login) Route
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            session['user'] = username
            return jsonify({"redirect": url_for('dashboard')})  # Redirect via JSON response
        else:
            return jsonify({"error": "Invalid credentials"}), 401  # Send error response
    return render_template('login_signup.html')

# Signup Route
@app.route('/signup', methods=['POST'])
def signup():
    full_name = request.form['full_name']
    doctor_id = request.form['doctor_id']
    hospital = request.form['hospital']
    specialization = request.form['specialization']
    username = request.form['new_username']
    email = request.form['email']
    password = request.form['new_password']

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (full_name, doctor_id, hospital, specialization, username, email, password) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (full_name, doctor_id, hospital, specialization, username, email, password))
        conn.commit()
        conn.close()
        return jsonify({"success": True, "message": "Signup successful! Please log in."})
    except sqlite3.IntegrityError:
        return jsonify({"success": False, "message": "This email is already registered. Please use a different email or log in."})

# Dashboard Route
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

# New Patient Route
@app.route('/new_patient', methods=['GET', 'POST'])
def new_patient():
    if 'user' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        eye_issue = request.form['eye_issue']
        diabetes = request.form['diabetes']
        duration = request.form['duration']
        image_file = request.files['image']
        diagnosed_by = session['user']

        if image_file:
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(image_path)

            # Process Image for CNN Model
            img_array = preprocess_image(image_path)
            prediction = model.predict(img_array)[0]
            insights = generate_insights(prediction)

            # Generate PDF Report
            pdf_report_path = generate_pdf(name, age, gender, eye_issue, diabetes, duration, image_path, insights)

            # Save to Database
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute("""INSERT INTO patients 
                        (name, age, gender, eye_issue, diabetes, duration, image_path, diagnosed_by, diagnosis_result, pdf_report_path) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                      (name, age, gender, eye_issue, diabetes, duration, image_path, diagnosed_by, "Pending", pdf_report_path))
            patient_id = c.lastrowid  # Get the ID of the newly inserted patient
            conn.commit()
            conn.close()

            # Redirect to result.html for this specific patient
            return redirect(url_for('view_patient', patient_id=patient_id))
    return render_template('new_patient.html')

# Upload file
@app.route('/uploads/<filename>')
def serve_pdf(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)


# Update Patient Record Route
@app.route('/update_patient/<int:patient_id>', methods=['POST'])
def update_patient(patient_id):
    if 'user' not in session:
        return redirect(url_for('login'))
    
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("UPDATE patients SET name=?, age=?, gender=?, eye_issue=?, diabetes=?, duration=?, diagnosis_result=? WHERE id=?",
              (request.form['name'], request.form['age'], request.form['gender'], request.form['eye_issue'], request.form['diabetes'], request.form['duration'], request.form['diagnosis_result'], patient_id))
    conn.commit()
    conn.close()
    
    return redirect(url_for('existing_patient'))

# Existing Patient Route
@app.route('/existing_patients')
def existing_patients():
    if 'user' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT id, name, age, gender, eye_issue, diabetes, duration, image_path FROM patients")
    patients = c.fetchall()
    conn.close()

    return render_template('existing_patients.html', patients=patients)

# View Patients Route
@app.route('/view_patient/<int:patient_id>')
def view_patient(patient_id):
    if 'user' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT name, age, gender, eye_issue, diabetes, duration, image_path, pdf_report_path FROM patients WHERE id=?", (patient_id,))
    patient = c.fetchone()
    conn.close()

    if not patient:
        return "Patient not found", 404

    name, age, gender, eye_issue, diabetes, duration, image_path, pdf_report_path = patient

    # Re-run the model to generate insights again (if needed)
    img_array = preprocess_image(image_path)
    prediction = model.predict(img_array)[0]
    insights = generate_insights(prediction)

    return render_template('result.html', name=name, age=age, gender=gender, eye_issue=eye_issue, diabetes=diabetes, duration=duration, pdf_report_path=pdf_report_path, insights=insights)

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)