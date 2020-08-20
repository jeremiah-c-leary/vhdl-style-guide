
from vsg.vhdlFile.classify import for_generate_statement
#from vsg.vhdlFile.classify import if_generate_statement
#from vsg.vhdlFile.classify import case_generate_statement


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    generate_statement ::=
        for_generate_statement
      | if_generate_statement
      | case_generate_statement
    '''
    if for_generate_statement.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def clear_flags(dVars):
    for_generate_statement.clear_flags(dVars)
