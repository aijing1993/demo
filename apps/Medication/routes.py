from apps.Patient.patient import Patient
from apps.Medication import blueprint, medication_service
from flask import render_template, request, jsonify, session
from flask_login import login_required
import json
from werkzeug.exceptions import HTTPException
from apps.Medication import medication

def get_patient_for_user():
    """
    """
    if 'username' in session: 
        username = session['username']

    patient = Patient.query.filter_by(username=username).first()

    return patient

@blueprint.route('/allMedications', methods=['GET'])
@login_required
def api_get_medications():
    """
    Get all patients
    :return:
    """
    medications = medication_service.get_all_medications()
  #  return render_template('patient.html', title='Patient')
    return jsonify([medication.get_medication() for medication in medications])

@blueprint.route('/patientMedications', methods=['GET'])
@login_required
def api_get_patient_medications():
    """
    Get all patients
    :return:
    """
    patient = get_patient_for_user()
    patient_medications = medication_service.get_user_medications()
  #  return render_template('patient.html', title='Patient')
    return jsonify([patient_medication.get_medication() for patient_medication in patient_medications])


