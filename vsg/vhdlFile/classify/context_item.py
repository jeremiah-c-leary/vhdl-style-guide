# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import context_reference, library_clause, use_clause


def detect(oDesignFile):
    """
    context_item ::=
        library_clause
      | use_clause
      | context_reference
    """

    if library_clause.detect(oDesignFile):
        return True

#    iCurrent = use_clause.detect(oDesignFile)
#    if iCurrent != iToken:
#        return iCurrent
#
#    iCurrent = context_reference.detect(iToken, lObjects)
#    if iCurrent != iToken:
#        return iCurrent
#
#    return iToken

    return False
