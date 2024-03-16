# -*- coding: utf-8 -*-

from vsg import parser


class architecture_keyword(parser.keyword):
    """
    unique_id = architecture_body : architecture_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class identifier(parser.identifier):
    """
    unique_id = architecture_body : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class of_keyword(parser.keyword):
    """
    unique_id = architecture_body : of_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class entity_name(parser.name):
    """
    unique_id = architecture_body : entity_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class is_keyword(parser.keyword):
    """
    unique_id = architecture_body : is_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class begin_keyword(parser.keyword):
    """
    unique_id = architecture_body : begin_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_keyword(parser.keyword):
    """
    unique_id = architecture_body : end_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_architecture_keyword(parser.keyword):
    """
    unique_id = architecture_body : end_architecture_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class architecture_simple_name(parser.simple_name):
    """
    unique_id = architecture_body : architecture_simple_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = architecture_body : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
