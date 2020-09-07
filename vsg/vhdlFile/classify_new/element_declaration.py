
from vsg.token import element_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import identifier_list
from vsg.vhdlFile.classify_new import element_subtype_definition

'''
    element_declaration ::=
        identifier_list : element_subtype_definition ;
'''


def classify(iToken, lObjects):
    iCurrent = identifier_list.classify(iToken, lObjects)

    iCurrent = utils.assign_next_token_required(':', token.colon, iCurrent, lObjects)

    iCurrent = utils.classify_subelement_until(';', element_subtype_definition, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
