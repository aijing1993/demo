from apps.Encounter import blueprint, encounter_service
from flask import render_template, request, jsonify
from flask_login import login_required
import json
from werkzeug.exceptions import HTTPException
from apps.Medication import medication


@blueprint.route('/allEncounters', methods=['GET'])
@login_required
def api_get_encounters():
    """
    Get all patients
    :return:
    """
    encounters = encounter_service.get_all_encounters()
  #  return render_template('patient.html', title='Patient')
    return jsonify([encounter.get_encounter() for encounter in encounters])