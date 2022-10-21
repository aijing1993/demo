from apps.Condition import blueprint, condition_service
from flask import render_template, request, jsonify
from flask_login import login_required
import json
from werkzeug.exceptions import HTTPException


@blueprint.route('/allConditions', methods=['GET'])
@login_required
def api_get_medications():
    """
    Get all patients
    :return:
    """
    conditions = condition_service.get_all_conditions()
  #  return render_template('patient.html', title='Patient')
    return jsonify([condition.get_condition() for condition in conditions])