# -*- coding: utf-8 -*-

from vsg import parser


class vunit_keyword(parser.keyword):
    """
    unique_id = psl_verification_unit : vunit_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class vpkg_keyword(parser.keyword):
    """
    unique_id = psl_verification_unit : vpkg_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class vprop_keyword(parser.keyword):
    """
    unique_id = psl_verification_unit : vprop_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class vmode_keyword(parser.keyword):
    """
    unique_id = psl_verification_unit : vmode_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class todo(parser.todo):
    """
    unique_id = psl_verification_unit : todo
    """

    def __init__(self, sString):
        super().__init__(sString)


class open_curly(parser.open_curly):
    """
    unique_id = psl_verification_unit : open_curly
    """

    def __init__(self, sString):
        super().__init__()


class close_curly(parser.close_curly):
    """
    unique_id = psl_verification_unit : close_curly
    """

    def __init__(self, sString):
        super().__init__()
