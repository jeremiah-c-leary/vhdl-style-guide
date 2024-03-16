# -*- coding: utf-8 -*-

from vsg import parser


class function_keyword(parser.keyword):
    """
    unique_id = function_specification : function_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class pure_keyword(parser.keyword):
    """
    unique_id = function_specification : pure_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class impure_keyword(parser.keyword):
    """
    unique_id = function_specification : impure_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class designator(parser.designator):
    """
    unique_id = function_specification : designator
    """

    def __init__(self, sString):
        super().__init__(sString)


class parameter_keyword(parser.keyword):
    """
    unique_id = function_specification : parameter_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class open_parenthesis(parser.open_parenthesis):
    """
    unique_id = function_specification : open_parenthesis
    """

    def __init__(self, sString="("):
        super().__init__()


class close_parenthesis(parser.close_parenthesis):
    """
    unique_id = function_specification : close_parenthesis
    """

    def __init__(self, sString=")"):
        super().__init__()


class return_keyword(parser.keyword):
    """
    unique_id = function_specification : return_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)
