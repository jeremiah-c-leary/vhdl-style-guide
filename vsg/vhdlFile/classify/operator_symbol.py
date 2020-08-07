
from vsg import parser

from vsg.vhdlFile.classify import string_literal


def check(oObject, iObject, lObjects, dVars):
    '''
    operator_symbol ::= string_literal
    '''
    if string_literal.check(oObject, iObject, lObjects, dVars):
        return True

    return False
