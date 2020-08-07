
from vsg import parser
from vsg.token import entity as token

from vsg.vhdlFile.classify import character_literal
from vsg.vhdlFile.classify import identifier
from vsg.vhdlFile.classify import identifier


def check(oObject, iObject, lObjects, dVars):
    '''
    identifier ::= basic_identifer | extended_identifier
    '''
    if type(oObject) == parser.item:
        return True

    return False
