# -*- coding: utf-8 -*-

from vsg import parser


class multiplying_operator(parser.keyword):
    """
    unique_id = multiplying_operator : multiplying_operator
    """

    def __init__(self, sString):
        super().__init__(sString)


class star(multiplying_operator):
    """
    unique_id = multiplying_operator : star
    """

    def __init__(self, sString="*"):
        super().__init__("*")


class slash(multiplying_operator):
    """
    unique_id = multiplying_operator : slash
    """

    def __init__(self, sString="/"):
        super().__init__("/")


class mod_operator(multiplying_operator):
    """
    unique_id = multiplying_operator : mod_operator
    """

    def __init__(self, sString):
        super().__init__(sString)


class rem_operator(multiplying_operator):
    """
    unique_id = multiplying_operator : rem_operator
    """

    def __init__(self, sString):
        super().__init__(sString)
