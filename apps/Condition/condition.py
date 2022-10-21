from flask import Flask, jsonify, request
from apps import db
import os


class Condition(db.Model):
    """ The data model"""
    # table name
    __tablename__ = 'Conditions'
    start = db.Column(db.DATE, nullable=False)
    stop = db.Column(db.DATE)
    patient = db.Column(db.String(200), primary_key=True, nullable=False)
    encounter = db.Column(db.String(200))
    code = db.Column(db.String(50))
    description = db.Column(db.String(300))


    def get_condition(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}