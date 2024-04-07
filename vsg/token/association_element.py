# -*- coding: utf-8 -*-

from vsg import parser


class assignment(parser.assignment):
    """
    unique_id = association_element : assignment
    """

    def __init__(self, sString):
        super().__init__(sString)


class formal_part(parser.item):
    """
    unique_id = association_element : formal_part
    """

    def __init__(self, sString):
        super().__init__(sString)


class actual_part(parser.item):
    """
    unique_id = association_element : actual_part
    """

    def __init__(self, sString):
        super().__init__(sString)
