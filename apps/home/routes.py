# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from apps.Patient import patient_service
from flask import render_template, request, session
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps.Medication import medication_service

@blueprint.route('/index')
@login_required
def index():
    if 'username' in session:
        username = session['username']
    test_list = patient_service.build_recommendation_test()
    fullname = patient_service.get_patient_name()
    counts = patient_service.get_patient_encounters()
    cp_counts = patient_service.get_patient_careplan()
    cost = patient_service.get_medical_costs()
    next_appt = patient_service.get_appointment()
    pcp_lname, contact = patient_service.get_pcp()
    health_plan, phone = patient_service.get_payer()
    medications = medication_service.get_user_medications()
    return render_template('home/index.html', segment='index', username=username, test_list=test_list, fullname = fullname, counts = counts,
    cp_counts = cp_counts, cost = cost, next_appt = next_appt, pcp_lname = pcp_lname, pcp_contact = contact, health_plan = health_plan, phone = phone,
    medications=medications)

@blueprint.route('/calendar')
@login_required
def calendar():
    if 'username' in session:
        username = session['username']
    fullname = patient_service.get_patient_name()
    return render_template('home/calendar.html', username=username, fullname = fullname)

@blueprint.route('/all_medications')
@login_required
def basic_table():
    if 'username' in session:
        username = session['username']
    fullname = patient_service.get_patient_name()
    all_medications = medication_service.get_user_all_medications()
    return render_template('home/all_medications.html', segment='all_medications', all_medications=all_medications, username=username, fullname = fullname)

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
