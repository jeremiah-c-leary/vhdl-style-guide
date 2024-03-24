# -*- coding: utf-8 -*-

from vsg import parser


class protected_keyword(parser.keyword):
    """
    unique_id = protected_type_body : protected_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class body_keyword(parser.keyword):
    """
    unique_id = protected_type_body : body_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_keyword(parser.keyword):
    """
    unique_id = protected_type_body : end_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_protected_keyword(parser.keyword):
    """
    unique_id = protected_type_body : end_protected_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_body_keyword(parser.keyword):
    """
    unique_id = protected_type_body : end_body_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class protected_type_simple_name(parser.simple_name):
    """
    unique_id = protected_type_body : protected_type_simple_name
    """

    def __init__(self, sString):
        super().__init__(sString)
