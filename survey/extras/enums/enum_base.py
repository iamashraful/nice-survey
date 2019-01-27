import enum

__author__ = 'Ashraful'


class EnumBase(enum.Enum):
    def __init__(self, **kwargs):
        super(EnumBase, self).__init__()

    @classmethod
    def get_model_choices(cls):
        pass
