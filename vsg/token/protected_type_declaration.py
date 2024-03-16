# -*- coding: utf-8 -*-

from vsg import parser


class protected_keyword(parser.keyword):
    """
    unique_id = protected_type_declaration : protected_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_keyword(parser.keyword):
    """
    unique_id = protected_type_declaration : end_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_protected_keyword(parser.keyword):
    """
    unique_id = protected_type_declaration : end_protected_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class protected_type_simple_name(parser.simple_name):
    """
    unique_id = protected_type_declaration : protected_type_simple_name
    """

    def __init__(self, sString):
        super().__init__(sString)
