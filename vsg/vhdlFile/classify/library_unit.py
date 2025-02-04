# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import primary_unit, secondary_unit


def detect(oDataStructure):
    """
    library_unit ::=
        primary_unit
      | secondary_unit
    """

    if primary_unit.detect(oDataStructure):
        return True


#    iCurrent = secondary_unit.detect(iToken, lObjects)
#    if iCurrent != iToken:
#        return iCurrent
#
#    return iToken
