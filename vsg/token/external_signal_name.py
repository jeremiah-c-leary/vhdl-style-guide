# -*- coding: utf-8 -*-

from vsg import parser


class double_less_than(parser.identifier):
    """
    unique_id = external_signal_name : double_less_than
    """

    def __init__(self, sString):
        super().__init__(sString)


class signal_keyword(parser.keyword):
    """
    unique_id = external_signal_name : signal_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class external_pathname(parser.keyword):
    """
    unique_id = external_signal_name : external_pathname
    """

    def __init__(self, sString):
        super().__init__(sString)


class colon(parser.colon):
    """
    unique_id = external_signal_name : colon
    """

    def __init__(self, sString=":"):
        super().__init__()


class double_greater_than(parser.identifier):
    """
    unique_id = external_signal_name : double_greater_than
    """

    def __init__(self, sString):
        super().__init__(sString)