
from vsg.vhdlFile.classify import package_body_declarative_item


def detect(iToken, lObjects):
    '''
    package_body_declarative_part ::=
        { package_body_declarative_item }
    '''

    iLast = 0
    iCurrent = iToken
    while iLast != iCurrent:
        iLast = iCurrent
        iCurrent = package_body_declarative_item.detect(iCurrent, lObjects)
    return iCurrent
