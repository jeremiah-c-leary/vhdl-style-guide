
from vsg.token import incomplete_type_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import identifier


def detect(iToken, lObjects):
    '''
    incomplete_type_declaration ::=
        type identifier ;
    '''
    if utils.are_next_consecutive_tokens(['type', None, ';'], iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('type', token.type_keyword, iToken, lObjects)

    iCurrent = identifier.classify(iCurrent, lObjects, token.identifier)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
