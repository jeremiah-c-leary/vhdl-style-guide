
from vsg.token import signal_kind as token

from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    '''
    signal_kind ::=
        register | bus
    '''

    if utils.is_next_token('register', iToken, lObjects):
        return classify(iToken, lObjects)
    elif utils.is_next_token('bus', iToken, lObjects):
        return classify(iToken, lObjects)

    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_if('register', token.register_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if('bus', token.register_bus, iToken, lObjects)

    return iCurrent
