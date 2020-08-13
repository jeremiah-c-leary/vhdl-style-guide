
from vsg.vhdlFile.classify import block_declarative_item


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    architecture_declarative_part ::=
    
        { block_declarative_item }
    
    '''

    if block_declarative_item.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def clear_flags(dVars):
    block_declarative_item.clear_flags(dVars)
