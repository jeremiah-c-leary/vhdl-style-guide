# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import context_clause, library_unit


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    design_unit ::=
        context_clause library_unit
    """
    if context_clause.detect(oDataStructure):
        return True

    return library_unit.detect(oDataStructure)
