from flask import Flask, jsonify, request
from apps import db
import os
from sqlalchemy.dialects.mssql import DATETIMEOFFSET

class Payer(db.Model):
    """ The data model"""
    # table name
    __tablename__ = 'Payers'

    id = db.Column(db.String(200), primary_key=True, nullable=False)
    name = db.Column(db.String(20))
    address = db.Column(db.String(200))
    city = db.Column(db.String(50))
    state_headquartered = db.Column(db.String(2))
    zip =  db.Column(db.String(10))
    phone = db.Column(db.String(20))
    amount_covered = db.Column(db.FLOAT)
    amount_uncovered = db.Column(db.FLOAT)
    revenue = db.Column(db.FLOAT)
    covered_encounters = db.Column(db.INTEGER)
    uncovered_encounters = db.Column(db.INTEGER)
    covered_medications = db.Column(db.INTEGER)
    uncovered_medications = db.Column(db.INTEGER)
    covered_procedures = db.Column(db.INTEGER)
    uncovered_procedures = db.Column(db.INTEGER)
    covered_immunizations = db.Column(db.INTEGER)
    uncovered_immunizations = db.Column(db.INTEGER)
    unique_customers = db.Column(db.INTEGER)
    qols_avg =  db.Column(db.FLOAT)
    member_months = db.Column(db.INTEGER)

    def get_payer(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
