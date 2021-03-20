
from vsg.vhdlFile.classify import configuration_declarative_item


def detect(iToken, lObjects):
    '''
    configuration_declarative_part ::=
        { configuration_declarative_item }
    '''

    iLast = 0
    iCurrent = iToken
    while iLast != iCurrent:
        iLast = iCurrent
        iCurrent = configuration_declarative_item.detect(iCurrent, lObjects)
    return iCurrent
