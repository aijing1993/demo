from apps.Patient import blueprint
from flask import render_template, request, jsonify, flash, session
from flask_login import login_required
from apps.Patient import patient_service
import json,random
from apps.Patient.patient import Patient
from werkzeug.exceptions import HTTPException
from apps import db
from apps.Patient.patientform import PatientProfile
# from flask_cors import CORS, cross_origin



@blueprint.route('/allPatients', methods=['GET'])
@login_required
def api_get_patients():
    """
    Get all patients
    :return:
    """
    patients = patient_service.get_all_patient()
  #  return render_template('patient.html', title='Patient')
    return jsonify([patient.get_patient() for patient in patients])


@blueprint.route('/patientImgLink', methods=['GET'])
@login_required
def api_get_patientImgLink():
    """
    Get all patients
    :return:
    """
    patient = patient_service.get_patient_for_user()
    patient_info = patient.get_patient()
    gender = patient_info['gender']
    patient_id = patient_service.get_patient_id_from_user_table()
    patient_id = patient_id
    if gender == "F":
        patient_imgLink = "https://randomuser.me/api/portraits/women/" + str(patient_id) + ".jpg"
        pcp_imgLink = "https://randomuser.me/api/portraits/women/" + str(patient_id+1) + ".jpg"
    else:
        patient_imgLink = "https://randomuser.me/api/portraits/men/" + str(patient_id) + ".jpg"
        pcp_imgLink = "https://randomuser.me/api/portraits/men/" + str(patient_id+1) + ".jpg"

    return jsonify([patient_imgLink, pcp_imgLink])


@blueprint.route('/patientProfile', methods=['GET'])
@login_required
def api_get_patientInfo():
    """
    Get all patients
    :return:
    """
    patient = patient_service.get_patient_for_user()
    fullname = patient_service.get_patient_name()
    pcp_lname,_ = patient_service.get_pcp()
    patient_info = patient.get_patient()
    patient_info["fullname"] = fullname
    patient_info["email"] = "M"
    patient_info["pcp_lname"] = pcp_lname
    if patient_info["fullname"] == "Jeffrey Greenfelder":
        patient_info["note1"] = ""
    return jsonify(patient_info)

@blueprint.route('/patientappointment', methods=['GET'])
@login_required
def api_get_patient_appointment():
    patient_appointments = patient_service.get_appointments()
    return jsonify([appointment.get_appointment() for appointment in patient_appointments])

@blueprint.route('/editPatientProfile', methods=('GET','POST'))
# @cross_origin()
def edit_patient_profile():
    if 'username' in session:
        username = session['username']
    my_patient_profile = patient_service.get_patient_profile_by_username(username)
    fullname = patient_service.get_patient_name()
    my_patient_profile.first = ''.join([i for i in my_patient_profile.first if not i.isdigit()])
    my_patient_profile.last = ''.join([i for i in my_patient_profile.last if not i.isdigit()])
    my_patient_profile.fullname = fullname
    profile_form = PatientProfile(obj=my_patient_profile)
    try:
        profile_form.populate_obj(my_patient_profile)
        print(profile_form.city.object_data)
        db.session.add(my_patient_profile)
        db.session.commit()
        print('saved successfully')

    except Exception as e:
        db.session.rollback()
        print(e)

    return render_template('home/forms_profile.html',form=profile_form, username=username, fullname=fullname)



