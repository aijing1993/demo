from apps.Patient.patient import Patient
from apps.Encounter.encounter import Encounter
from apps.Careplan.careplan import Careplan
from apps.Medication.medication import Medication
from apps.Appointment.appointment import Appointment
from apps.Provider.provider import Provider
from apps.Payer.payer import Payer
from apps.authentication.models import Users
from flask import session
from datetime import date
from sqlalchemy.sql import func

all_test = {'F': {'younger_than_20': [['Growth (height and weight)', 'yearly'], ['Blood Pressure Screening', 'every 2 years'], ['Eye Exam', 'every 1-2 years'], ['Hearing Test', 'every 10 years']], '20s': [['Eye Exam', 'every 1-2 years'], ['Hearing Test', 'every 10 years'], ['Blood Pressure Screening', 'every 2 years'], ['Skin Exam', 'yearly'], ['Pelvic Exam', 'yearly'], ['Pap Smear', 'every 3 years']], '30s': [['Blood Pressure Screening', 'every 2 years'], ['Skin Exam', 'yearly'], ['Pelvic Exam', 'yearly'], ['Pap Smear', 'every 3 years'], ['Blood Glucose Test', 'every 5 years'], ['Cholesterol Screening', 'every 5 years'], ['Thyroid Stimulating Hormone Test', 'every few years']], '40s': [['Blood Pressure Screening', 'every 2 years'], ['Skin Exam', 'yearly'], ['Pelvic Exam', 'yearly'], ['Pap Smear', 'every 3 years'], ['Blood Glucose Test', 'every 5 years'], ['Cholesterol Screening', 'every 5 years'], ['Bone Density Testing', 'every 3 years'], ['Mammogram', 'yearly'], ['Ovarian Screening', 'every 3 years']], '50s': [['Blood Pressure Screening', 'every 2 years'], ['Pelvic Exam', 'yearly'], ['Pap Smear', 'every 3 years'], ['Blood Glucose Test', 'every 5 years'], ['Cholesterol Screening', 'every 5 years'], ['Bone Density Testing', 'every 3 years'], ['Mammogram', 'yearly'], ['Ovarian Screening', 'every 3 years'], ['Coronary Screening', 'yearly'], ['Colonoscopy', 'every 10 years'], ['Fecal Occult Blood Test', 'yearly']], '60s_and_older': [['Blood pressure screening', 'every 2 years'], ['Pelvic exam', 'every year'], ['Pap smear', 'every 3 years'], ['Blood Glucose Test', 'every 5 years'], ['Cholesterol Screening', 'every 5 years'], ['Colonoscopy', 'every 10 years'], ['Colorectal Screening', 'every 5 years'], ['Ovarian Screening', 'every 3 years'], ['Coronary Screening', 'yearly'], ['Fecal Occult Blood Test', 'yearly'], ['Bone Density Testing', 'every 3 years'], ['Herpes Booster', 'once'], ['Pneumonia', 'once']]}, 'M': {'younger_than_20': [['Growth (height and weight)', 'yearly'], ['Blood Pressure Screening', 'every 2 years'], ['Eye Exam', 'every 1-2 years'], ['Hearing Test', 'every 10 years']], '20s': [['Eye Exam', 'every 1-2 years'], ['Hearing Test', 'every 10 years'], ['Blood Pressure Screening', 'every 2 years'], ['Skin Exam', 'yearly'], ['Testicular Exam', 'yearly']], '30s': [['Blood Pressure Screening', 'every 2 years'], ['Skin Exam', 'yearly'], ['Testicular Exam', 'yearly'], ['Blood Glucose Test', 'every 5 years'], ['Cholesterol Screening', 'every 5 years']], '40s': [['Blood Pressure Screening', 'every 2 years'], ['Skin Exam', 'yearly'], ['Testicular Exam', 'yearly'], ['Blood Glucose Test', 'every 5 years'], ['Cholesterol Screening', 'every 5 years'], ['Prostate Exam', "per doctor's suggestion"]], '50s': [['Blood Pressure Screening', 'every 2 years'], ['Testicular Exam', 'yearly'], ['Blood Glucose Test', 'every 5 years'], ['Cholesterol Screening', 'every 5 years'], ['Colonoscopy', 'every 10 years'], ['Prostate Screening', 'every 3 years']], '60s_and_older': [['Blood pressure screening', 'every 2 years'], ['Blood Glucose Test', 'every 5 years'], ['Cholesterol Screening', 'every 5 years'], ['Colonoscopy', 'every 10 years'], ['Coronary Screening', 'yearly'], ['Prostate Screening', 'every 3 years'], ['Testicular Exam', 'every 3 years'], ['Herpes Booster', 'once'], ['Pneumonia', 'once']]}}

def get_all_patients():
    """
    """
    return Patient.query.all()


def get_patient_for_user():
    """
    """
    if 'username' in session: 
        username = session['username']

    patient = Patient.query.filter_by(username=username).first()

    return patient

def get_patient_id_from_user_table():
    """
    """
    if 'username' in session: 
        username = session['username']    
    user = Users.query.filter_by(username=username).first()
    patient_id = user.id
    if patient_id > 1099:
        patient_id = patient_id - 1100
    elif patient_id > 999:
        patient_id = patient_id - 1000
    elif patient_id > 100:
        patient_id = patient_id // 10
    return patient_id

def build_recommendation_test():
    """
    """
    patient = get_patient_for_user()
    patient_info = patient.get_patient()
    birthdate = patient_info['birthdate']
    gender = patient_info['gender']
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    if 20<= age < 30:
        age_group = '20s'
    elif 30<= age < 40:
        age_group = '30s'
    elif 40<= age < 50:
        age_group = '40s'
    elif 50<= age < 60:
        age_group = '50s'
    elif age >= 60:
        age_group = '60s_and_older'
    else:
        age_group = 'younger_than_20'

    test_list = all_test[gender][age_group]
    return test_list


def get_patient_name():
    """
    """   
    patient = get_patient_for_user()
    return ''.join([i for i in patient.first if not i.isdigit()]) + ' ' + ''.join([i for i in patient.last if not i.isdigit()])    


def get_patient_encounters():
    """
    """ 
    if 'username' in session: 
        username = session['username']

    counts = Patient.query.filter_by(username=username).join(Encounter, (Patient.id == Encounter.patient)).count()
    return counts
    
def get_patient_careplan():
    """
    """ 
    if 'username' in session: 
        username = session['username']

    cp_counts = Patient.query.filter_by(username=username).join(Careplan, (Patient.id == Careplan.patient)).count()
    return cp_counts
    
def get_medical_costs():
    """
    """ 
    if 'username' in session: 
        username = session['username']
    
    patient = get_patient_for_user()
    patient = patient.id
    cost1 = Encounter.query.with_entities(func.sum(Encounter.total_claim_cost-Encounter.payer_coverage).label('cost')).filter(Encounter.patient == patient).first()
    cost2 = Medication.query.with_entities(func.sum(Medication.totalcost)).filter(Medication.patient == patient).first()
    return round(cost1[0]+cost2[0], 1)
    
def get_appointment():
    """
    """ 
    if 'username' in session: 
        username = session['username']
    
    patient = get_patient_for_user()
    patient = patient.id
    date = Appointment.query.filter_by(patient = patient).first()
    if date is None:
       date = 'No appointment'
    else:
       date = date.start
    return date
    
def get_pcp():
    """
    """ 
    patient = get_patient_for_user()
    patient = patient.id
    pcp = Encounter.query.filter_by(patient = patient).order_by(Encounter.start.desc()).first()
    pcp_info = Provider.query.filter_by(id = pcp.provider).first()
    lname = ''.join([i for i in pcp_info.name.split(" ")[1] if not i.isdigit()])
    
    #contact
    contact = "Hello, this is your PCP, {}. I am specialized in {}. Here is the address of my office: {}".format(''.join([i for i in pcp_info.name if not i.isdigit()]), pcp_info.speciality.lower(), pcp_info.address.title() +', '+pcp_info.city.title() + ', ' + pcp_info.state + ' ' + pcp_info.zip)
    return lname, contact
    
def get_payer():
    """
    """ 
    patient = get_patient_for_user()
    patient = patient.id
    payer = Encounter.query.filter_by(patient = patient).order_by(Encounter.start.desc()).first()
    payer_info = Payer.query.filter_by(id = payer.payer).first()
    return payer_info.name, payer_info.phone

def get_appointments():
    if 'username' in session:
        username = session['username']

    patient = get_patient_for_user()
    patient = patient.id
    appts = Appointment.query.filter_by(patient=patient)
    return appts

def get_patient_profile_by_username(username):
    patient = Patient.query.filter_by(username=username).first()

    return patient