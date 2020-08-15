
from vsg import parser

from vsg.token import assertion_statement as token

from vsg.vhdlFile.classify import assertion


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    assertion_statement ::= [ label : ] assertion ;
    '''

    if dVars['assertion_statement']:
        if classify_semicolon(oObject, iObject, lObjects, dVars):
            return True

    if assertion.tokenize(oObject, iObject, lObjects, dVars):
        dVars['assertion_statement'] = True
        return True

    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == ';':
        lObjects[iObject] = token.semicolon()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    dVars['assertion_statement'] = False
    assertion.clear_flags(dVars)
