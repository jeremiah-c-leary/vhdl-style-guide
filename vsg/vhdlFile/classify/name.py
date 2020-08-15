
from vsg import parser


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    name ::=
        simple_name
      | operator_symbol
      | character_literal
      | selected_name
      | indexed_name
      | slice_name
      | attribute_name
      | external_name
    '''
    if type(oObject) == parser.item:
        return True

    return False


def clear_flags(dVars):
    return True
