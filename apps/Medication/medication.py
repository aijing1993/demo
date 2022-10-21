from flask import Flask, jsonify, request
from apps import db

import os


class Medication(db.Model):
    """ The data model"""
    # table name
    __tablename__ = 'Medications'
    start = db.Column(db.DateTime, nullable=False, primary_key=True)
    stop = db.Column(db.DateTime)
    patient = db.Column(db.String(200), nullable=False)
    payer = db.Column(db.String(200))
    encounter = db.Column(db.String(200))
    code = db.Column(db.String(50))
    description = db.Column(db.String(300))
    base_cost = db.Column(db.FLOAT)
    payer_coverage = db.Column(db.FLOAT)
    dispenses = db.Column(db.FLOAT)
    totalcost = db.Column(db.FLOAT)
    reasoncode = db.Column(db.String(100))
    reasondescription = db.Column(db.String(300))

    def get_medication(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}