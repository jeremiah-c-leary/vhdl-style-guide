# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import context_clause, library_unit


def detect(oDataStructure):
    """
    design_unit ::=
        context_clause library_unit
    """
    if context_clause.detect(oDataStructure):
        return True

    return library_unit.detect(oDataStructure)
