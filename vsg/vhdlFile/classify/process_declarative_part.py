

from vsg.vhdlFile.classify import process_declarative_item


def detect(iToken, lObjects):
    '''
    process_declarative_part ::=
        { process_declarative_item }
    '''

    iLast = 0
    iCurrent = iToken
    while iLast != iCurrent:
        iLast = iCurrent
        iCurrent = process_declarative_item.detect(iCurrent, lObjects)
    return iCurrent
