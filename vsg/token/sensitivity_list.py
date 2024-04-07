# -*- coding: utf-8 -*-

from vsg import parser


class comma(parser.comma):
    """
    unique_id = sensitivity_list : comma
    """

    def __init__(self, sString=","):
        super().__init__()
