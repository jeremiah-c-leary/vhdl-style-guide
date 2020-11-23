
from vsg.token import element_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import element_subtype_definition
from vsg.vhdlFile.classify import identifier_list


def classify(iToken, lObjects):
    '''
    element_declaration ::=
        identifier_list : element_subtype_definition ;
    '''

    iCurrent = identifier_list.classify_until([':'], iToken, lObjects)

    iCurrent = utils.assign_next_token_required(':', token.colon, iCurrent, lObjects)

    iCurrent = element_subtype_definition.classify_until([';'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
