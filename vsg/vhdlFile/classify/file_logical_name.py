
from vsg.vhdlFile.classify import expression


def classify(iToken, lObjects):
    '''
    file_logical_name ::= *string*_expression
    '''

    iCurrent = expression.classify_until([';'], iToken, lObjects)

    return iCurrent
