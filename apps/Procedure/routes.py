from apps.Procedure import blueprint, procedure_service
from flask import render_template, request, jsonify
from flask_login import login_required
import json
from werkzeug.exceptions import HTTPException


@blueprint.route('/allProcedures', methods=['GET'])
@login_required
def api_get_procedures():
    """
    Get all patients
    :return:
    """
    procedures = procedure_service.get_all_procedure()
  #  return render_template('patient.html', title='Patient')
    return jsonify([procedure.get_procedure() for procedure in procedures])