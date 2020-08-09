
from vsg import parser
from vsg.token import vhdl_range as token


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    range ::= 
        range_attribute_name
      | simple_expression direction simple_expression
    ''' 

    if classify_range(oObject, iObject, lObjects, dVars):
        return True 

    return False


def classify_range(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item and oObject.get_value() != ';':
        lObjects[iObject] = token.vhdl_range(oObject.get_value())
        return True
    return False


def clear_flags(dVars):
    return
