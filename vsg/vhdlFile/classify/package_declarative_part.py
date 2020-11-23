
from vsg.vhdlFile.classify import package_declarative_item


def detect(iToken, lObjects):
    '''
    package_declarative_part ::=
        { package_declarative_item }
    '''

    iLast = 0
    iCurrent = iToken
    while iLast != iCurrent:
        iLast = iCurrent
        iCurrent = package_declarative_item.detect(iCurrent, lObjects)
    return iCurrent
