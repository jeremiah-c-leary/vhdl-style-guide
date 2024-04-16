# -*- coding: utf-8 -*-

from vsg import parser


class logical_operator(parser.keyword):
    """
    unique_id = logical_operator : logical_operator
    """

    def __init__(self, sString):
        super().__init__(sString)


class and_operator(logical_operator):
    """
    unique_id = logical_operator : and_operator
    """

    def __init__(self, sString):
        super().__init__(sString)


class or_operator(logical_operator):
    """
    unique_id = logical_operator : or_operator
    """

    def __init__(self, sString):
        super().__init__(sString)


class nand_operator(logical_operator):
    """
    unique_id = logical_operator : nand_operator
    """

    def __init__(self, sString):
        super().__init__(sString)


class nor_operator(logical_operator):
    """
    unique_id = logical_operator : nor_operator
    """

    def __init__(self, sString):
        super().__init__(sString)


class xor_operator(logical_operator):
    """
    unique_id = logical_operator : xor_operator
    """

    def __init__(self, sString):
        super().__init__(sString)


class xnor_operator(logical_operator):
    """
    unique_id = logical_operator : xnor_operator
    """

    def __init__(self, sString):
        super().__init__(sString)
