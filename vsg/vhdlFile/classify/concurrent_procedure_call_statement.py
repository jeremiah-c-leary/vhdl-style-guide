
from vsg import parser

from vsg.token import concurrent_procedure_call_statement as token

from vsg.vhdlFile.classify import procedure_call


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    concurrent_procedure_call_statement ::=
    [ label : ] [ postponed ] procedure_call ;
    '''

    if dVars['concurrent_procedure_call_statement']:
        if classify_semicolon(oObject, iObject, lObjects, dVars):
            return True

    if procedure_call.tokenize(oObject, iObject, lObjects, dVars):
        dVars['concurrent_procedure_call_statement'] = True
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
    dVars['concurrent_procedure_call_statement'] = False
    procedure_call.clear_flags(dVars)
