
from vsg.token import signature as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import type_mark


def detect(iToken, lObjects):
    '''
    signature ::= **[** [ type_mark { , type_mark } ] [ return type_mark ] **]**

    NOTE:  The [ and ] enclosed by ** are required if the signature is provided.
    '''

    if utils.is_next_token('[', iToken, lObjects):
        return classify(iToken, lObjects)

    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('[', token.open_bracket, iToken, lObjects)

    detect_type_mark(iCurrent, lObjects)

    detect_return(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(']', token.close_bracket, iCurrent, lObjects)

    return iCurrent


def detect_return(iToken, lObjects):

    iCurrent = iToken
    if utils.is_next_token('return', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('return', token.return_keyword, iCurrent, lObjects)
        iCurrent = type_mark.classify(iCurrent, lObjects)
    return iCurrent


def detect_type_mark(iToken, lObjects):

    iCurrent = iToken
    if not utils.is_next_token('return', iCurrent, lObjects):
        iCurrent = type_mark.classify(iCurrent, lObjects)
        while utils.is_next_token(',', iCurrent, lObjects):
            iCurrent = utils.assign_next_token_required(',', token.comma, iCurrent, lObjects)
            iCurrent = type_mark.classify(iCurrent, lObjects)

    return iCurrent
