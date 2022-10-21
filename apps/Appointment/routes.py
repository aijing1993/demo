from apps.Appointment import blueprint, appointment_service
from flask import render_template, request, jsonify
from flask_login import login_required
import json
from werkzeug.exceptions import HTTPException


@blueprint.route('/allAppointments', methods=['GET'])
@login_required
def api_get_appointments():
    """
    Get all patients
    :return:
    """
    appointments = appointment_service.get_all_appointments()
  #  return render_template('patient.html', title='Patient')
    return jsonify([appointment.get_appointment() for appointment in appointments])
  #   return jsonify({"start" : "11-1-2022"})