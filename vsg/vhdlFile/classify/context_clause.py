
from vsg.vhdlFile.classify import context_item


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    context_clause ::= { context_item }
    '''

    if context_item.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def clear_flags(dVars):
    context_item.clear_flags(dVars)
