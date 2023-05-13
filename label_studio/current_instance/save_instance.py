from organizations.models import Organization

class CurrentInstance:

    CURRENT_ORGANIZATION = None
    CURRENT_USER=None
    CURRENT_USER_ROLE=None

    def __init__(self):
        pass

    @classmethod
    def set_current_organization(cls, organ):
        cls.CURRENT_ORGANIZATION=organ


    @classmethod
    def get_current_organization(cls):
        return cls.CURRENT_ORGANIZATION


