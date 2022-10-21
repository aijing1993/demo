from flask import Flask, jsonify, request
from apps import db
import os


class Patient(db.Model):
    """ The data model"""
    # table name
    __tablename__ = 'Patients'

    id = db.Column(db.String(200), primary_key=True, nullable=False)
    birthdate = db.Column(db.DATE, nullable=False)
    deathdate = db.Column(db.DATE)
    ssn = db.Column(db.String(15))
    drivers = db.Column(db.String(30))
    passport = db.Column(db.String(30))
    prefix = db.Column(db.String(10))
    first = db.Column(db.String(30), nullable= False)
    last = db.Column(db.String(30), nullable=False)
    suffix = db.Column(db.String(30))
    maiden = db.Column(db.String(30))
    marital = db.Column(db.String(30))
    race = db.Column(db.String(50))
    ethnicity = db.Column(db.String(50))
    gender = db.Column(db.String(2), nullable= False)
    birthplace = db.Column(db.String(250))
    address = db.Column(db.String(250))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    county = db.Column(db.String(50))
    zip = db.Column(db.INTEGER)
    lat = db.Column(db.FLOAT)
    lon = db.Column(db.FLOAT)
    healthcare_expenses = db.Column(db.FLOAT)
    healthcare_coverage = db.Column(db.FLOAT)
    username = db.Column(db.String(50))


    def get_patient(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
