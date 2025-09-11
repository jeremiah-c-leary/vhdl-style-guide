# -*- coding: utf-8 -*-
from vsg import parser


class comma(parser.comma):
    """
    unique_id = record_element_list : comma
    """

    def __init__(self, sString=","):
        super().__init__()


class simple_name(parser.simple_name):
    """
    unique_id = record_element_list : record_element_simple_name
    """

    def __init__(self, sString):
        super().__init__(sString)
