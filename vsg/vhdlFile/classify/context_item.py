# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import context_reference, library_clause, use_clause


def detect(oDataStructure):
    """
    context_item ::=
        library_clause
      | use_clause
      | context_reference
    """

    if library_clause.detect(oDataStructure):
        return True

    #    iCurrent = use_clause.detect(oDataStructure)
    #    if iCurrent != iToken:
    #        return iCurrent
    #
    #    iCurrent = context_reference.detect(iToken, lObjects)
    #    if iCurrent != iToken:
    #        return iCurrent
    #
    #    return iToken

    return False
