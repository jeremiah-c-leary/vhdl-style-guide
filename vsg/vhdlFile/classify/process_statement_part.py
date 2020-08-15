
from vsg.vhdlFile.classify import sequential_statement


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    process_statement_part ::=
        { sequential_statement }
    '''
    if sequential_statement.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def clear_flags(dVars):
    sequential_statement.clear_flags(dVars)
