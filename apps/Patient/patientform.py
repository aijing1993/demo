from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField
from wtforms.validators import DataRequired, Email, Length

class PatientProfile(FlaskForm):
    first = StringField('First Name', validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])
    last = StringField('Last Name', validators=[DataRequired(), Length(min=-1, max=80,
                                                                         message='You cannot have more than 80 characters')])
    gender = SelectField('Biological sex', choices=[('M','M'),('F','F')])
    birthdate = DateField('Date of Birth')
    address = StringField('Address')
    city = StringField('City')
    state = StringField('State')
    county = StringField('County')
