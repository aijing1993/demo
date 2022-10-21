from flask import Flask, jsonify, request
from apps import db
import os


class Encounter(db.Model):
    """ The data model"""
    # table name
    __tablename__ = 'Encounters'

    id = db.Column(db.String(200), nullable=False, primary_key=True)
    start = db.Column(db.TIMESTAMP)
    stop = db.Column(db.TIMESTAMP)
    patient = db.Column(db.String(200), nullable=False)
    organization = db.Column(db.String(200))
    provider= db.Column(db.String(200))
    payer = db.Column(db.String(200))
    encounterclass = db.Column(db.String(100))
    code = db.Column(db.String(50))
    description = db.Column(db.String(200))
    base_encounter_cost = db.Column(db.FLOAT)
    total_claim_cost = db.Column(db.FLOAT)
    payer_coverage = db.Column(db.FLOAT)
    reasoncode = db.Column(db.String(100))
    reasondescription = db.Column(db.String(300))

    def get_encounter(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}