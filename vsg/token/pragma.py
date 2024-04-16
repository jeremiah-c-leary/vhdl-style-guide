# -*- coding: utf-8 -*-

from vsg import parser


class ignore(parser.item):
    """
    unique_id = pragma : ignore
    """

    def __init__(self, sString):
        super().__init__(sString)


class pragma(parser.comment):
    """
    unique_id = pragma : pragma
    """

    def __init__(self, sString):
        super().__init__(sString)


class open(pragma):
    """
    unique_id = pragma : open
    """

    def __init__(self, sString):
        super().__init__(sString)


class close(pragma):
    """
    unique_id = pragma : close
    """

    def __init__(self, sString):
        super().__init__(sString)


class single(pragma):
    """
    unique_id = pragma : single
    """

    def __init__(self, sString):
        super().__init__(sString)
