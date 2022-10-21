from apps.Patient.patient import Patient
from apps.Observation import blueprint, observation_service
from flask import render_template, request, jsonify, session
from flask_login import login_required
import json
from werkzeug.exceptions import HTTPException

def get_patient_for_user():
    """
    """
    if 'username' in session: 
        username = session['username']

    patient = Patient.query.filter_by(username=username).first()

    return patient

@blueprint.route('/allObservations', methods=['GET'])
@login_required
def api_get_observations():
    """
    Get all patients
    :return:
    """
    observations = observation_service.get_all_observation()
  #  return render_template('patient.html', title='Patient')
    return jsonify([observation.get_observation() for observation in observations])

@blueprint.route('/pressureLow', methods=['GET'])
@login_required
def api_get_blood_pressure_low():
    """
    Get all patients
    :return:
    """
    patient = get_patient_for_user()
    pressure_low = observation_service.get_blood_pressure_low(patient.id)
  #  return render_template('patient.html', title='Patient')
    return jsonify([ob_pressure.get_observation() for ob_pressure in pressure_low])


@blueprint.route('/pressureHigh', methods=['GET'])
@login_required
def api_get_blood_pressure_high():
    """
    Get all patients
    :return:
    """
    patient = get_patient_for_user()
    pressure_high = observation_service.get_blood_pressure_high(patient.id)
  #  return render_template('patient.html', title='Patient')
    return jsonify([ob_pressure.get_observation() for ob_pressure in pressure_high])