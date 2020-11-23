
from vsg.token import full_type_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import identifier
from vsg.vhdlFile.classify import type_definition


def detect(iToken, lObjects):
    '''
    full_type_declaration ::=
        type identifier is type_definition ;
    '''

    if utils.are_next_consecutive_tokens(['type', None, 'is'], iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('type', token.type_keyword, iToken, lObjects)

    iCurrent = identifier.classify(iCurrent, lObjects, token.identifier)

    iCurrent = utils.assign_next_token_required('is', token.is_keyword, iCurrent, lObjects)

    iCurrent = type_definition.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
