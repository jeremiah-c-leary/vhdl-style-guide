# -*- coding: utf-8 -*-

from vsg import parser


class configuration_keyword(parser.keyword):
    """
    unique_id = configuration_body : configuration_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class identifier(parser.identifier):
    """
    unique_id = configuration_body : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class of_keyword(parser.keyword):
    """
    unique_id = configuration_body : of_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class entity_name(parser.name):
    """
    unique_id = configuration_body : entity_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class is_keyword(parser.keyword):
    """
    unique_id = configuration_body : is_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_keyword(parser.keyword):
    """
    unique_id = configuration_body : end_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_configuration_keyword(parser.keyword):
    """
    unique_id = configuration_body : end_configuration_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class configuration_simple_name(parser.simple_name):
    """
    unique_id = configuration_body : configuration_simple_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = configuration_body : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
