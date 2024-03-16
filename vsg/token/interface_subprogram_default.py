# -*- coding: utf-8 -*-
from vsg import parser


class subprogram_name(parser.name):
    """
    unique_id = interface_subprogram_default : subprogram_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class undefined_range(parser.undefined_range):
    """
    unique_id = interface_subprogram_default : undefined_range
    """

    def __init__(self, sString="<>"):
        super().__init__()
