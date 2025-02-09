# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import range_constraint


def detect(oDataStructure):
    """
    integer_type_definition ::=
        range_constraint
    """

    range_constraint.detect(oDataStructure)
