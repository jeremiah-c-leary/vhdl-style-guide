
from vsg.token import interface_incomplete_type_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import identifier


def detect(iToken, lObjects):
    '''
    interface_incomplete_type_declaration ::=
        type identifier
    '''
    if utils.is_next_token('type', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_if('type', token.type_keyword, iToken, lObjects)
    iCurrent = identifier.classify(iCurrent, lObjects)

    return iCurrent
