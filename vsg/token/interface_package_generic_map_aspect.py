# -*- coding: utf-8 -*-

from vsg import parser


class generic_keyword(parser.keyword):
    """
    unique_id = interface_package_generic_map_aspect : generic_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class map_keyword(parser.keyword):
    """
    unique_id = interface_package_generic_map_aspect : map_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class open_parenthesis(parser.open_parenthesis):
    """
    unique_id = interface_package_generic_map_aspect : open_parenthesis
    """

    def __init__(self, sString="("):
        super().__init__()


class default_keyword(parser.keyword):
    """
    unique_id = interface_package_generic_map_aspect : default_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class undefined_range(parser.undefined_range):
    """
    unique_id = interface_package_generic_map_aspect : undefined_range
    """

    def __init__(self, sString="<>"):
        super().__init__()


class close_parenthesis(parser.close_parenthesis):
    """
    unique_id = interface_package_generic_map_aspect : close_parenthesis
    """

    def __init__(self, sString=")"):
        super().__init__()
