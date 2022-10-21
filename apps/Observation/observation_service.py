from apps.Observation.observation import Observation


def get_all_observation():
    """
    Get all patients
    :return:
    """
    return Observation.query.all()

def get_blood_pressure_low(patient):
    return Observation.query.filter_by(patient=patient).filter(Observation.code.like('8462-4')).order_by(Observation.date.desc()).limit(2).all()


def get_blood_pressure_high(patient):
    return Observation.query.filter_by(patient=patient).filter(Observation.code.like('8480-6')).order_by(Observation.date.desc()).limit(2).all()