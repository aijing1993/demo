from flask import Flask, jsonify, request
from apps import db
import os
from sqlalchemy.dialects.mssql import DATETIMEOFFSET

class Provider(db.Model):
    """ The data model"""
    # table name
    __tablename__ = 'Providers'

    id = db.Column(db.String(200), primary_key=True, nullable=False)
    organization = db.Column(db.String(200))
    name = db.Column(db.String(20))
    gender = db.Column(db.String(1))
    speciality = db.Column(db.String(20))
    address = db.Column(db.String(200))
    city = db.Column(db.String(50))
    state =  db.Column(db.String(2))
    zip =  db.Column(db.String(10))
    lat = db.Column(db.FLOAT)
    lon = db.Column(db.FLOAT)
    utilization = db.Column(db.INTEGER)

    def get_provider(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
