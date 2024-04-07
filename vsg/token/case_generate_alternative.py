# -*- coding: utf-8 -*-

from vsg import parser


class alternative_label_name(parser.label):
    """
    unique_id = case_generate_alternative : alternative_label_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class alternative_label_colon(parser.label_colon):
    """
    unique_id = case_generate_alternative : alternative_label_colon
    """

    def __init__(self):
        super().__init__()


class when_keyword(parser.keyword):
    """
    unique_id = case_generate_alternative : when_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class assignment(parser.assignment):
    """
    unique_id = case_generate_alternative : assignment
    """

    def __init__(self, sString):
        super().__init__(sString)
