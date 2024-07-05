# -*- coding: utf-8 -*-

from vsg import parser


class open_bracket(parser.open_bracket):
    """
    unique_id = signature : open_bracket
    """

    def __init__(self, sString="["):
        super().__init__("[")


class return_keyword(parser.keyword):
    """
    unique_id = signature : return_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class comma(parser.comma):
    """
    unique_id = signature : comma
    """

    def __init__(self, sString=","):
        super().__init__()


class close_bracket(parser.close_bracket):
    """
    unique_id = signature : close_bracket
    """

    def __init__(self, sString="]"):
        super().__init__("]")
