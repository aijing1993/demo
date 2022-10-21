from flask import Flask, jsonify, request
from apps import db
import os


class Careplan(db.Model):
    """ The data model"""
    # table name
    __tablename__ = 'Careplans'

    id = db.Column(db.String(200), primary_key=True, nullable=False)
    start = db.Column(db.DATE)
    stop = db.Column(db.DATE)
    patient = db.Column(db.String(200), nullable=False)
    encounter = db.Column(db.String(200))
    code = db.Column(db.String(50))
    description = db.Column(db.String(200))
    reasoncode = db.Column(db.String(100))
    reasondescription = db.Column(db.String(300))

    def get_careplan(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}