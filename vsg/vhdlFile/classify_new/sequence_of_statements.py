
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import sequential_statement

'''
    sequence_of_statements ::=
        { sequential_statement }
'''


def detect(iToken, lObjects):
    iLast = 0
    iCurrent = iToken
    while iLast != iCurrent:
        iLast = iCurrent
        iCurrent = sequential_statement.detect(iCurrent, lObjects)
    return iCurrent
