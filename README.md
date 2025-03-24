Diagnosis of Diabetic Retinopathy using CNN 
Problem Statement: 

DR is one of the major causes of visual impairment among diabetic patients worldwide. The complications are grave, but early detection and treatment can prevent them; however, accessing specialized eye care is limited in many parts of the world, especially in remote and under-resourced regions. Traditional diagnosis methods are cumbersome, expensive, and dependent on specialists, delaying diagnosis and thus treatment. 
Project Strategy 

This strategy emphasizes using CNNs for addressing the major requirement for DR accurate diagnosis in a friendly and accessible way. With AI techniques being applied in scalable platforms, the project can be an initiative towards transformation of eye care in less-endowed parts and advance boundaries for AI research as well. 
Project Purpose 
 Detect DR accurately from fundus images. (internal images) 
Provide early intervention opportunities to prevent blindness. 
Enhance healthcare accessibility by minimizing dependency on specialists. 
Improve diagnostic efficiency for clinicians with multi-condition assessments. 
Project Vision 

To revolutionize diabetic retinopathy diagnosis and eye health assessment by creating an accessible, accurate, and scalable AI-powered solution, reducing preventable blindness globally. 
Project Mission 
Design and deploy an AI-based system that uses CNNs to offer early and accurate DR detection, personalized progression monitoring, and comprehensive eye health analysis, all to ensure equitable healthcare for all, especially for the underserved. 
Use Case 1: Automated Diabetic Retinopathy Screening
•	Goal: Provide a model for diabetic retinopathy (DR) in clinics without access to eye specialists. 
•	How: Use a CNN-based model to analyse fundus images and detect DR in real-time.  
•	Impact: Enables early detection, reducing the risk of blindness and ensuring timely treatment. 
Use Case 2: Monitoring Disease Progression 
•	Goal: Track the progression of diabetic retinopathy in patients over time. 
•	How: Combine CNNs and LSTMs to analyse chronological fundus images and predict whether the condition is improving or worsening. Integrate patient data for personalized monitoring. 
•	Impact: Helps healthcare providers adjust treatments early and improve patient outcomes. 
Use Case 3: Comprehensive Eye Health Analysis 
•	Goal: Diagnose diabetic retinopathy along with other eye conditions like glaucoma and macular enema. 
•	How: Use a multi-task CNN model to identify multiple conditions from a single fundus image, with separate outputs for each diagnosis. 
•	Impact: Provides a holistic eye health assessment, saving time and improving diagnostic efficiency for healthcare providers. 
 
Tactics 

To achieve the projects goals, these tactics will be implemented: 
1. Technology Development 
	• 	Use transfer learning with pre-trained CNNs (e.g., ResNet) to reduce development time. 
2.	Data and Model Preparation 
•	Collect and preprocess fundus image datasets from sources like Kaggle  
•	Perform data augmentation (e.g., rotation, brightness adjustments) to improve model generalization. 
•	Use balanced training datasets to address class imbalances. 
3.	Deployment Strategy 
•	Remote Screening: Develop a lightweight mobile or web-based application for deployment in clinics without access to specialists. 
•	Progress Monitoring: Build a dashboard for clinicians to track disease progression and generate patient-specific insights. 
4.	Evaluation and Optimization 
•	Use metrics like accuracy, recall, and AUC-ROC to evaluate model performance. 
•	Optimize the model for deployment on edge devices (e.g., smartphones) for offline accessibility. 
5.	Collaboration and User Training 
•	Partner with healthcare providers to validate the system in real-world settings. 
•	Train clinicians and staff to use the system effectively and interpret results. 
 


(2) Highlight on how our project is relevant to people, industry, the environment, culture, the economy:

Use Case 1: Automated Diabetic Retinopathy Screening
Relevance:
•	People: Enables individuals access early screening and treatment, reducing the risk of blindness due to late-stage diabetic retinopathy.
•	Industry: Healthcare providers and telemedicine companies can expand their services and improve patient outreach, creating business opportunities.
•	Environment: Reduces the need for frequent long-distance travel to specialized medical centres, decreasing carbon emissions and environmental impact.
•	Culture: Encourages health awareness and proactive management of diabetes-related complications within communities that traditionally lack access to specialized healthcare.
•	Economy: Cost-effective screening solutions help reduce the financial burden on healthcare systems by detecting the disease early and preventing expensive late-stage treatments.


Use Case 2: Monitoring Disease Progression
Relevance:
•	People: Provides diabetic patients with continuous monitoring to track disease progression, empowering them with actionable insights for lifestyle and treatment adjustments.
•	Industry: Pharmaceutical companies and medical device manufacturers can leverage AI-driven data to develop targeted treatments and personalized medication plans.
•	Environment: Digital record-keeping minimizes the use of paper-based medical records, contributing to sustainability efforts in healthcare.
•	Culture: Encourages a shift toward preventive healthcare culture, promoting regular eye health check-ups and reducing diabetes-related stigma.
•	Economy: Reduces healthcare costs by preventing complications through early detection and continuous tracking, leading to fewer hospital admissions and lower insurance claims.

Use Case 3: Comprehensive Eye Health Analysis
Relevance:
•	People: Expands beyond diabetic retinopathy to detect other vision-related disorders such as glaucoma and cataracts, improving overall eye health management.
•	Industry: Optical clinics, hospitals, and insurance companies can integrate AI-based comprehensive diagnostic tools to enhance service offerings and patient care.
•	Environment: Efficient and automated AI diagnostics reduce the need for physical medical infrastructure, optimizing resources and lowering waste.
•	Culture: Promotes a holistic approach to eye care, encouraging communities to prioritize routine screenings and eye health education.
•	Economy: Boosts productivity by minimizing vision-related work disabilities and absenteeism, contributing to a more efficient workforce.


(3) Use cases Citations:

Use Case 1: Automated Diabetic Retinopathy Screenin
Natarajan, S., Jain, A., Krishnan, R., Rogye, A., & Sivaprasad, S. (2019). Diagnostic accuracy of Community-Based diabetic retinopathy screening with an offline artificial intelligence system on a smartphone. JAMA Ophthalmology, 137(10), 1182. https://doi.org/10.1001/jamaophthalmol.2019.2923
Smartphone Funduscopy - How to Use Smartphone to Take Fundus Photographs - EyeWiki

Use Case 2: Monitoring Disease Progression 
Aronno, D. G., & Saeha, S. (2025, January 4). Diabetic Retinopathy Detection Using CNN with Residual Block with DCGAN. arXiv.org. https://arxiv.org/abs/2501.02300

Use Case 3: Comprehensive Eye Health Analysis 
Rafay, A., Asghar, Z., Manzoor, H., & Hussain, W. (2023). EyeCNN: exploring the potential of convolutional neural networks for identification of multiple eye diseases through retinal imagery. International Ophthalmology, 43(10), 3569–3586. https://doi.org/10.1007/s10792-023-02764-5


(4) Justification of Use Cases for Diabetic Retinopathy Diagnosis Using CNNs:
1. Automated Diabetic Retinopathy Screening
Compelling Argument:
One of the biggest challenges in combating diabetic retinopathy (DR) is the lack of accessibility to specialized eye care. CNN-based automated screening solutions provide an efficient and scalable approach to addressing this challenge by leveraging teleophthalmology. These systems can analyse retinal images taken with low-cost portable fundus cameras and provide accurate diagnoses without requiring an ophthalmologist on-site.
Why This Use Case is Critical:
•	Accessibility: More than 50% of the global diabetic population lives in areas with limited access to ophthalmologists. Automated screening can bridge the gap.
•	Scalability: AI models can be deployed in primary healthcare centres or mobile health clinics to conduct mass screenings.
•	Cost Efficiency: Automated diagnosis reduces the need for in-person specialist consultations, cutting down healthcare costs for both patients and healthcare providers.
•	Timely Detection: Early-stage DR often goes undetected in underserved areas, leading to irreversible vision loss. AI-powered tools ensure timely interventions and reduce blindness rates.

2. Monitoring Disease Progression
Compelling Argument:
Diabetic Retinopathy is a progressive condition, with its severity worsening over time if left unchecked. Continuous monitoring using CNN-based solutions allows for real-time tracking of disease progression, enabling doctors to personalize treatment plans based on objective and quantifiable changes in retinal images.
Why This Use Case is Critical:
•	Early Intervention: Monitoring enables early detection of changes, preventing complications such as macular edema and proliferative DR.
•	Personalized Treatment: AI systems can provide insights into the progression trend, helping doctors tailor treatments (e.g., laser therapy, injections, or lifestyle interventions).
•	Reduction in Hospital Visits: Patients can have their eyes monitored remotely, reducing the need for frequent hospital visits and ensuring adherence to screening guidelines.
•	Integration with Wearables and Cloud-Based Systems: Advances in technology allow AI to integrate with mobile health apps, helping patients stay informed about their eye health regularly.

3. Comprehensive Eye Health Analysis
Compelling Argument:
Beyond diabetic retinopathy, other vision-threatening conditions such as glaucoma, cataracts, and age-related macular degeneration (AMD) are major concerns. A comprehensive CNN-based eye health analysis tool can provide multi-disease detection, ensuring holistic eye care management.
Why This Use Case is Critical:
•	Early Detection of Multiple Conditions: Many eye diseases have overlapping symptoms and risk factors; an AI-driven comprehensive analysis can catch early signs of multiple diseases.
•	Improved Diagnostic Accuracy: CNN models trained on large datasets can differentiate between various eye conditions with high precision, reducing misdiagnosis.
•	Preventive Healthcare: Patients at risk (e.g., elderly, hypertensive, or with genetic predispositions) can benefit from routine AI-driven screenings to maintain long-term eye health.
•	Healthcare Efficiency: Streamlining the diagnostic process by using a single model for multiple conditions reduces the workload on specialists and speeds up patient management.
•	Economic Impact: Preventing multiple eye diseases at an early stage can significantly cut healthcare costs associated with late-stage interventions and surgeries.
Conclusion
Implementing these CNN-based solutions for diabetic retinopathy diagnosis and comprehensive eye care will revolutionize how healthcare systems manage eye health by:
•	Ensuring equitable access to screening and monitoring tools.
•	Providing personalized treatment plans, improving patient compliance and clinical outcomes.
•	Offering a holistic approach to eye health by detecting multiple diseases, optimizing healthcare resources, and reducing economic burdens.
These use cases represent a forward-thinking, cost-effective, and patient-centric approach, supporting global efforts to prevent vision loss and enhance overall healthcare quality.




Setup and Run Instructions

Install Python
https://www.python.org/downloads/

Clone the Repository 
- git clone -b Use-Case-1 https://github.com/syed1917/Diagnosis-of-Diabetic-Retinopathy-using-CNN
- cd Diagnosis-of-Diabetic-Retinopathy-using-CNN

Create Virtual Environment & Install Dependencies 
- python -m venv dr_venv
- .\dr_venv\Scripts\Activate.ps1
- pip install flask fpdf pillow tensorflow

Run the Flask Application 
- python dev/app.py

Access the Application in the Browser 
- http://127.0.0.1:5000/



Notes
- Ensure the diabetic_retinopathy_model.h5 file is in the project directory.
- The uploads/ folder should have written permissions for storing images and PDFs.
- Logging is enabled to capture server activity.
- We used 50 epochs to train the CNN model, and we were not able to use more epochs due to computational barriers.
- After diagnosis, a PDF report is generated using FPDF and stored for clinician review.
- The report contains AI-generated insights, risk assessment, and follow-up recommendations.
