# -*- coding: utf-8 -*-

from vsg import parser


class shift_operator(parser.keyword):
    """
    unique_id = shift_operator : shift_operator
    """

    def __init__(self, sString):
        super().__init__(sString)


class sll(shift_operator):
    """
    unique_id = shift_operator : sll
    """

    def __init__(self, sString):
        super().__init__(sString)


class srl(shift_operator):
    """
    unique_id = shift_operator : srl
    """

    def __init__(self, sString):
        super().__init__(sString)


class sla(shift_operator):
    """
    unique_id = shift_operator : sla
    """

    def __init__(self, sString):
        super().__init__(sString)


class sra(shift_operator):
    """
    unique_id = shift_operator : sra
    """

    def __init__(self, sString):
        super().__init__(sString)


class rol(shift_operator):
    """
    unique_id = shift_operator : rol
    """

    def __init__(self, sString):
        super().__init__(sString)


class ror(shift_operator):
    """
    unique_id = shift_operator : ror
    """

    def __init__(self, sString):
        super().__init__(sString)
