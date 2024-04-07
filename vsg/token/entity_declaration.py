# -*- coding: utf-8 -*-

from vsg import parser


class entity_keyword(parser.keyword):
    """
    unique_id = entity_declaration : entity_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class identifier(parser.identifier):
    """
    unique_id = entity_declaration : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class is_keyword(parser.keyword):
    """
    unique_id = entity_declaration : is_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class begin_keyword(parser.keyword):
    """
    unique_id = entity_declaration : begin_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_keyword(parser.keyword):
    """
    unique_id = entity_declaration : end_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_entity_keyword(parser.keyword):
    """
    unique_id = entity_declaration : end_entity_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class entity_simple_name(parser.simple_name):
    """
    unique_id = entity_declaration : entity_simple_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = entity_declaration : semicolon
    """

    def __init__(self, sString):
        super().__init__()
