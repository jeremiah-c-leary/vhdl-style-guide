
from vsg.vhdlFile.classify import concurrent_statement


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    architecture_statement_part ::=
    
        { concurrent_statement }
    
    '''

    if concurrent_statement.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def clear_flags(dVars):
    concurrent_statement.clear_flags(dVars)
