
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import subprogram_declarative_item

'''
    subprogram_declarative_part ::=
        { subprogram_declarative_item }
'''


def detect(iToken, lObjects):
    iLast = 0
    iCurrent = iToken
    while iLast != iCurrent:
        iLast = iCurrent
        iCurrent = subprogram_declarative_item.detect(iCurrent, lObjects)
    return iCurrent
