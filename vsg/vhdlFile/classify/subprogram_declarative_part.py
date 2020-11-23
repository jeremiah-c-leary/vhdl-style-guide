
from vsg.vhdlFile.classify import subprogram_declarative_item


def detect(iToken, lObjects):
    '''
    subprogram_declarative_part ::=
        { subprogram_declarative_item }
    '''

    iLast = 0
    iCurrent = iToken
    while iLast != iCurrent:
        iLast = iCurrent
        iCurrent = subprogram_declarative_item.detect(iCurrent, lObjects)
    return iCurrent
