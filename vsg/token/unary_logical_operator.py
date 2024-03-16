# -*- coding: utf-8 -*-

from vsg import parser


class unary_logical_operator(parser.keyword):
    """
    unique_id = unary_logical_operator : unary_logical_operator
    """

    def __init__(self, sString):
        super().__init__(sString)


class and_operator(unary_logical_operator):
    """
    unique_id = unary_logical_operator : and_operator
    """

    def __init__(self, sString):
        super().__init__(sString)


class or_operator(unary_logical_operator):
    """
    unique_id = unary_logical_operator : or_operator
    """

    def __init__(self, sString):
        super().__init__(sString)


class nand_operator(unary_logical_operator):
    """
    unique_id = unary_logical_operator : nand_operator
    """

    def __init__(self, sString):
        super().__init__(sString)


class nor_operator(unary_logical_operator):
    """
    unique_id = unary_logical_operator : nor_operator
    """

    def __init__(self, sString):
        super().__init__(sString)


class xor_operator(unary_logical_operator):
    """
    unique_id = unary_logical_operator : xor_operator
    """

    def __init__(self, sString):
        super().__init__(sString)


class xnor_operator(unary_logical_operator):
    """
    unique_id = unary_logical_operator : xnor_operator
    """

    def __init__(self, sString):
        super().__init__(sString)
