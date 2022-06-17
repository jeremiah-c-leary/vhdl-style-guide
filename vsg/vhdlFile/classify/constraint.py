
from vsg.vhdlFile.classify import range_constraint
from vsg.vhdlFile.classify import array_constraint
from vsg.vhdlFile.classify import record_constraint


def detect(iToken, lObjects):
    '''
    constraint ::=
        range_constraint
      | array_constraint
      | record_constraint
    '''

    iReturn = range_constraint.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = array_constraint.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = record_constraint.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return iToken
