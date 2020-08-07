
from vsg import parser


def check(oObject, iObject, lObjects, dVars):
    '''
    string_literal ::= " { graphic_character } "
    '''

    if type(oObject) == parser.item and oObject.get_value().startswith('"') and oObject.get_value().endswith('"'):
        return True

    return False
