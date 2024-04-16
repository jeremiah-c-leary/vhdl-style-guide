# -*- coding: utf-8 -*-

from vsg import parser


class instantiation_label(parser.label):
    """
    unique_id = component_instantiation_statement : instantiation_label
    """

    def __init__(self, sString):
        super().__init__(sString)


class label_colon(parser.label_colon):
    """
    unique_id = component_instantiation_statement : label_colon
    """

    def __init__(self):
        super().__init__()


class semicolon(parser.semicolon):
    """
    unique_id = component_instantiation_statement : semicolon
    """

    def __init__(self, sString=None):
        super().__init__()
