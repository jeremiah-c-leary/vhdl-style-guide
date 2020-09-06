
from vsg.token import full_type_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import identifier
from vsg.vhdlFile.classify_new import type_definition

'''
    full_type_declaration ::=
        type identifier is type_definition ;
'''


def detect(iToken, lObjects):
    if utils.is_next_token('type', iToken, lObjects):
        if utils.find_in_next_n_tokens('is', 3, iToken, lObjects):
            return classify(iToken, lObjects)
        else:
            return iToken
    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required('type', token.type_keyword, iToken, lObjects)
    iCurrent = identifier.classify(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('is', token.is_keyword, iCurrent, lObjects)
    iCurrent = type_definition.detect(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)
    return iCurrent
