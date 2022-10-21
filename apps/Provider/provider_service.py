from apps.Provider.provider import Provider


def get_all_provider():
    """
    Get all patients
    :return:
    """
    return Provider.query.all()
