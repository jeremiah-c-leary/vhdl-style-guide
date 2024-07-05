# -*- coding: utf-8 -*-

from vsg import parser


class entity_keyword(parser.keyword):
    """
    unique_id = entity_aspect : entity_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class entity_name(parser.name):
    """
    unique_id = entity_aspect : entity_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class open_parenthesis(parser.open_parenthesis):
    """
    unique_id = process_statement : open_parenthesis
    """

    def __init__(self, sString="("):
        super().__init__()


class architecture_identifier(parser.identifier):
    """
    unique_id = entity_aspect : architecture_identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class close_parenthesis(parser.close_parenthesis):
    """
    unique_id = process_statement : close_parenthesis
    """

    def __init__(self, sString=")"):
        super().__init__()


class configuration_keyword(parser.keyword):
    """
    unique_id = entity_aspect : configuration_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class configuration_name(parser.name):
    """
    unique_id = entity_aspect : configuration_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class open_keyword(parser.keyword):
    """
    unique_id = entity_aspect : open_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)
