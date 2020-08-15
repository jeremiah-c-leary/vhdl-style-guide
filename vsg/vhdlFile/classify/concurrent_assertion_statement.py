
from vsg import parser

from vsg.token import concurrent_assertion_statement as token

from vsg.vhdlFile.classify import assertion


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    concurrent_assertion_statement ::=
        [ label : ] [ postponed ] assertion ;
    '''

    if dVars['concurrent_assertion_statement']:
        if classify_semicolon(oObject, iObject, lObjects, dVars):
            return True

    if assertion.tokenize(oObject, iObject, lObjects, dVars):
        dVars['concurrent_assertion_statement'] = True
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
    dVars['concurrent_assertion_statement'] = False
    assertion.clear_flags(dVars)
