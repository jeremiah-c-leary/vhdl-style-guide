# -*- coding: utf-8 -*-

from vsg import parser


class transport_keyword(parser.keyword):
    """
    unique_id = delay_mechanism : transport_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class inertial_keyword(parser.keyword):
    """
    unique_id = delay_mechanism : inertial_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class reject_keyword(parser.keyword):
    """
    unique_id = delay_mechanism : reject_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)
