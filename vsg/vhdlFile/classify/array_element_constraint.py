# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import element_constraint


def detect(oDataStructure):
    """
    array_element_constraint ::= element_constraint
    """
    return element_constraint.detect(oDataStructure)
