from apps.Careplan.careplan import Careplan


def get_all_careplans():
    """
    Get all patients
    :return:
    """
    return Careplan.query.all()