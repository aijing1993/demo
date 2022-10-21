from apps.Encounter.encounter import Encounter


def get_all_encounters():
    """
    Get all patients
    :return:
    """
    return Encounter.query.all()
