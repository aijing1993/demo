from apps.Patient.patient import Patient
from apps.Medication.medication import Medication
from flask import session


def get_all_medications():
    """
    Get all patients
    :return:
    """
    return Medication.query.all()


def get_patient_for_user():
    """
    """
    if 'username' in session:
        username = session['username']

    patient = Patient.query.filter_by(username=username).first()

    return patient


def get_user_medications():
    patient = get_patient_for_user().id
    return Medication.query.filter_by(patient=patient).limit(10).all()


def get_user_all_medications():
    patient = get_patient_for_user().id
    return Medication.query.filter_by(patient=patient).all()
