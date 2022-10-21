from flask import Flask, jsonify, request
from apps import db
import os


class Observation(db.Model):
    """ The data model"""
    # table name
    __tablename__ = 'Observations'

    date = db.Column(db.DATETIME, nullable=False, primary_key=True)
    patient = db.Column(db.String(200), nullable=False)
    encounter = db.Column(db.String(200), nullable=False)
    code = db.Column(db.String(100))
    description = db.Column(db.String(300))
    value = db.Column(db.String(50))
    units = db.Column(db.String(50))
    type = db.Column(db.String(30))


    def get_observation(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}