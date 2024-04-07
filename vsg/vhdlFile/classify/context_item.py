# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import context_reference, library_clause, use_clause


def detect(iToken, lObjects):
    """
    context_item ::=
        library_clause
      | use_clause
      | context_reference
    """

    iCurrent = library_clause.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = use_clause.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = context_reference.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    return iToken
