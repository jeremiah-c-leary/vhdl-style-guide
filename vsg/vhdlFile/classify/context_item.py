# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import context_reference, library_clause, use_clause
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    context_item ::=
        library_clause
      | use_clause
      | context_reference
    """

    if library_clause.detect(oDataStructure):
        return True

    if use_clause.detect(oDataStructure):
        return True

    return context_reference.detect(oDataStructure)
