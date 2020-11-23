
from vsg.vhdlFile.classify import sequential_statement


def detect(iToken, lObjects):
    '''
    sequence_of_statements ::=
        { sequential_statement }
    '''

    iLast = 0
    iCurrent = iToken
    while iLast != iCurrent:
        iLast = iCurrent
        iCurrent = sequential_statement.detect(iCurrent, lObjects)
    return iCurrent
