
from vsg.token import signal_kind as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import expression
from vsg.vhdlFile.classify_new import identifier_list
from vsg.vhdlFile.classify_new import signal_kind
from vsg.vhdlFile.classify_new import subtype_indication


'''
    signal_kind ::=
        register | bus
'''


def detect(iToken, lObjects):

    if utils.is_next_token('register', iToken, lObjects):
        return classify(iToken, lObjects)
    elif utils.is_next_token('bus', iToken, lObjects):
        return classify(iToken, lObjects)

    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_if('register', token.register_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if('bus', token.register_bus, iToken, lObjects)
    return iCurrent 
