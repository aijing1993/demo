from apps.Payer.payer import Payer


def get_all_payer():
    """
    Get all patients
    :return:
    """
    return Payer.query.all()
