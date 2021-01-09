
from vsg.token import file_open_information as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import expression


def classify(iToken, lObjects):
    '''
    file_logical_name ::= *string*_expression
    '''

    iCurrent = expression.classify_until([';'], iToken, lObjects)

    return iCurrent
