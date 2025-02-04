# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import context_clause, library_unit


def detect(oDesignFile):
    """
    design_unit ::=
        context_clause library_unit
    """
    if context_clause.detect(oDesignFile):
        return True

#    if library_unit.detect(oDesignFile):
#        return True

    return False
