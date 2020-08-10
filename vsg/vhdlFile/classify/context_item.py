
from vsg.vhdlFile.classify import use_clause


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    context_item ::=
        library_clause
      | use_clause
      | context_reference
    '''
    if use_clause.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def clear_flags(dVars):
    use_clause.clear_flags(dVars)
