# Diagnosis-of-Diabetic-Retinopathy-using-CNN

Setup and Run Instructions

Install Python
https://www.python.org/downloads/

Clone the Repository 
1.	git clone -b Use-Case-1 https://github.com/syed1917/Diagnosis-of-Diabetic-Retinopathy-using-CNN
2.	cd Diagnosis-of-Diabetic-Retinopathy-using-CNN

Create Virtual Environment & Install Dependencies 
3.	python -m venv dr_venv
4.	.\dr_venv\Scripts\Activate.ps1
5.	pip install flask fpdf pillow tensorflow

Run the Flask Application 
6.	python dev/app.py

Access the Application in the Browser 
7.	http://127.0.0.1:5000/



Notes
•	Ensure the diabetic_retinopathy_model.h5 file is in the project directory.
•	The uploads/ folder should have written permissions for storing images and PDFs.
•	Logging is enabled to capture server activity.
•	We used 50 epochs to train the CNN model, and we were not able to use more epochs due to computational barriers.
•	After diagnosis, a PDF report is generated using FPDF and stored for clinician review.
•	The report contains AI-generated insights, risk assessment, and follow-up recommendations.
