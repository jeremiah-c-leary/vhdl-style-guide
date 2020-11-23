
from vsg.vhdlFile.classify import context_clause
from vsg.vhdlFile.classify import library_unit


def detect(iToken, lObjects):
    '''
    design_unit ::=
        context_clause library_unit
    '''
    iCurrent = context_clause.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = library_unit.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    return iToken
