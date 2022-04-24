class Person:
    '''sample dostring
    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        msg (str): Human readable string describing the exception.
        code (:obj:`int`, optional): Error code.

    Attributes:
        msg (str): Human readable string describing the exception.
        code (int): Exception error code.
    '''

    def __init__(self, name, age):
        self.name = name
        self.age = age
