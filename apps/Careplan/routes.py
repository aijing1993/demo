from apps.Careplan import blueprint, careplan_service
from flask import render_template, request, jsonify
from flask_login import login_required
import json
from werkzeug.exceptions import HTTPException


@blueprint.route('/allCareplans', methods=['GET'])
@login_required
def api_get_careplans():
    """
    Get all patients
    :return:
    """
    careplans = careplan_service.get_all_careplans()
  #  return render_template('patient.html', title='Patient')
    return jsonify([careplan.get_careplan() for careplan in careplans])