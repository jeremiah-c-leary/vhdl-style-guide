
from vsg.vhdlFile.classify import process_declarative_item

def tokenize(oObject, iObject, lObjects, dVars):
    '''
    process_declarative_part ::=
        { process_declarative_item }
    '''
    if process_declarative_item.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def clear_flags(dVars):
    process_declarative_item.clear_flags(dVars)
