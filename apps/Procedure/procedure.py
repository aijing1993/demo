from flask import Flask, jsonify, request
from apps import db
import os
from sqlalchemy.dialects.mssql import DATETIMEOFFSET

class Procedure(db.Model):
    """ The data model"""
    # table name
    __tablename__ = 'Procedures'

    date = db.Column(db.DATETIME, nullable=False)
    patient = db.Column(db.String(200), primary_key=True, nullable=False)
    encounter = db.Column(db.String(200), nullable=False)
    code = db.Column(db.String(100))
    description = db.Column(db.String(300))
    base_cost = db.Column(db.FLOAT)
    reasoncode = db.Column(db.String(100))
    reasondescription = db.Column(db.String(300))

    def get_procedure(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}