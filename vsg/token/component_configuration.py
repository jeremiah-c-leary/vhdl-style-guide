# -*- coding: utf-8 -*-

from vsg import parser


class for_keyword(parser.keyword):
    """
    unique_id = component_configuration : for_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class binding_indication_semicolon(parser.semicolon):
    """
    unique_id = component_configuration : binding_indication_semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()


class end_keyword(parser.keyword):
    """
    unique_id = component_configuration : end_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_for_keyword(parser.keyword):
    """
    unique_id = component_configuration : end_for_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = component_configuration : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
