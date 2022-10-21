from apps.Provider import blueprint, provider_service
from flask import render_template, request, jsonify
from flask_login import login_required
import json
from werkzeug.exceptions import HTTPException


@blueprint.route('/allProvider', methods=['GET'])
@login_required
def api_get_providers():
    """
    Get all providers
    :return:
    """
    providers = provider_service.get_all_provider()
  #  return render_template('patient.html', title='Patient')
    return jsonify([provider.get_provider() for provider in providers])
