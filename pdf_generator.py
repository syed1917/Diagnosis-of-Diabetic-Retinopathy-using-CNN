from fpdf import FPDF
import os

def generate_pdf(name, age, gender, eye_issue, diabetes, duration, image_path, insights, output_dir='uploads'):
    os.makedirs(output_dir, exist_ok=True)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Diabetic Retinopathy Diagnosis Report", ln=True, align='C')
    pdf.ln(10)

    # Patient Details
    pdf.cell(100, 10, f"Patient Name: {name}", ln=True)
    pdf.cell(100, 10, f"Age: {age}", ln=True)
    pdf.cell(100, 10, f"Gender: {gender}", ln=True)
    pdf.cell(100, 10, f"Previous Eye Issues: {eye_issue}", ln=True)
    pdf.cell(100, 10, f"Diabetes: {diabetes}", ln=True)
    pdf.cell(100, 10, f"Diabetes Duration: {duration} years", ln=True)

    if os.path.exists(image_path):
        pdf.image(image_path, x=140, y=30, w=50)
        pdf.ln(60)

    pdf.cell(0, 10, "____________________________________________________", ln=True, align='C')
    pdf.ln(3)

    for key, value in insights.items():
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(0, 10, f"{key.replace('_', ' ').title()}:", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, f"{value}\n")
        pdf.ln(5)

    filename = f"{name.replace(' ', '_')}_diagnosis_report.pdf"
    pdf_path = os.path.join(output_dir, filename)
    pdf.output(pdf_path)
    return filename
