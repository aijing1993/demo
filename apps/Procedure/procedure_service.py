from apps.Procedure.procedure import Procedure


def get_all_procedure():
    """
    Get all patients
    :return:
    """
    return Procedure.query.all()