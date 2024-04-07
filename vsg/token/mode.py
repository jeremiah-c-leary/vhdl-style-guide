# -*- coding: utf-8 -*-

from vsg import parser


class mode(parser.keyword):
    """
    unique_id = mode : mode
    """

    def __init__(self, sString):
        super().__init__(sString)


class in_keyword(mode):
    """
    unique_id = mode : in_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class out_keyword(mode):
    """
    unique_id = mode : out_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class inout_keyword(mode):
    """
    unique_id = mode : inout_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class buffer_keyword(mode):
    """
    unique_id = mode : buffer_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class linkage_keyword(mode):
    """
    unique_id = mode : linkage_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)
