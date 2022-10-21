from apps.Appointment.appointment import Appointment


def get_all_appointments():
    """
    Get all patients
    :return:
    """
    return Appointment.query.order_by(Appointment.start).limit(1).all()

