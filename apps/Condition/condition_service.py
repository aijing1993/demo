from apps.Condition.condition import Condition


def get_all_conditions():
    """
    Get all patients
    :return:
    """
    return Condition.query.all()
