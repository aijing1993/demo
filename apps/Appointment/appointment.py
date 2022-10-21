from flask import Flask, jsonify, request
from apps import db
import os


class Appointment(db.Model):
    """ The data model"""
    # table name
    __tablename__ = 'Appointments'
    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    start = db.Column(db.DATE)
    stop = db.Column(db.DATE)
    patient = db.Column(db.String(200), nullable=False)
    appointment = db.Column(db.String(200))

    def get_appointment(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}