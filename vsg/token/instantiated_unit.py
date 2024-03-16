# -*- coding: utf-8 -*-

from vsg import parser


class component_keyword(parser.keyword):
    """
    unique_id = instantiated_unit : component_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class component_name(parser.name):
    """
    unique_id = instantiated_unit : component_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class entity_keyword(parser.keyword):
    """
    unique_id = instantiated_unit : entity_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class library_name(parser.name):
    """
    unique_id = instantiated_unit : library_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class dot(parser.dot):
    """
    unique_id = instantiated_unit : dot
    """

    def __init__(self, sString):
        super().__init__(sString)


class entity_name(parser.name):
    """
    unique_id = instantiated_unit : entity_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class open_parenthesis(parser.open_parenthesis):
    """
    unique_id = instantiated_unit : open_parenthesis
    """

    def __init__(self, sString="("):
        super().__init__()


class architecture_identifier(parser.identifier):
    """
    unique_id = instantiated_unit : architecture_identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class close_parenthesis(parser.close_parenthesis):
    """
    unique_id = instantiated_unit : close_parenthesis
    """

    def __init__(self, sString=")"):
        super().__init__()


class configuration_keyword(parser.keyword):
    """
    unique_id = instantiated_unit : configuration_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class configuration_name(parser.name):
    """
    unique_id = instantiated_unit : configuration_name
    """

    def __init__(self, sString):
        super().__init__(sString)
