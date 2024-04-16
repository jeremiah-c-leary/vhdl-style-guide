# -*- coding: utf-8 -*-

from vsg import parser


class rising_edge(parser.function):
    """
    unique_id = ieee_std_logic_1164_function : rising_edge
    """

    def __init__(self, sString):
        super().__init__(sString)


class falling_edge(parser.function):
    """
    unique_id = ieee_std_logic_1164_function : falling_edge
    """

    def __init__(self, sString):
        super().__init__(sString)
