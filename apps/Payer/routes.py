from apps.Payer import blueprint, payer_service
from flask import render_template, request, jsonify
from flask_login import login_required
import json
from werkzeug.exceptions import HTTPException


@blueprint.route('/allPayer', methods=['GET'])
@login_required
def api_get_payers():
    """
    Get all payers
    :return:
    """
    payers = payer_service.get_all_payer()
  #  return render_template('patient.html', title='Patient')
    return jsonify([payer.get_payer() for payer in payers])
