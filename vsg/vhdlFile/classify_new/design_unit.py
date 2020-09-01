
from vsg.vhdlFile.classify_new import context_clause
from vsg.vhdlFile.classify_new import library_unit


def detect(iCurrent, lObjects):
    '''
    design_unit ::=
        context_clause library_unit
    '''
    iReturned = context_clause.detect(iCurrent, lObjects)
    if iReturned != iCurrent:
        return iReturned

    iReturned = library_unit.detect(iCurrent, lObjects)
    if iReturned != iCurrent:
        return iReturned

    return iCurrent
