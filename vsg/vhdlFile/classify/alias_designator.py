
from vsg.token import alias_declaration as token

from vsg.vhdlFile.classify import character_literal
from vsg.vhdlFile.classify import identifier
from vsg.vhdlFile.classify import operator_symbol


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    alias_designator ::= identifier | character_literal | operator_symbol
    '''

    if character_literal.check(oObject, iObject, lObjects, dVars):
        lObjects[iObject] = token.character_literal(oObject.get_value())
        return True

    if operator_symbol.check(oObject, iObject, lObjects, dVars):
        lObjects[iObject] = token.operator_symbol(oObject.get_value())
        return True

    if identifier.check(oObject, iObject, lObjects, dVars):
        lObjects[iObject] = token.identifier(oObject.get_value())
        return True

    return False
