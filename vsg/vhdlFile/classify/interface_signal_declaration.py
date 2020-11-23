

from vsg.token import interface_signal_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import expression
from vsg.vhdlFile.classify import identifier_list
from vsg.vhdlFile.classify import mode
from vsg.vhdlFile.classify import subtype_indication


def detect(iToken, lObjects):
    '''
    interface_signal_declaration ::=
        [ signal ] identifier_list : [ mode ] subtype_indication [ bus ] [ := *static*_expression ]
    '''

    if utils.is_next_token('signal', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('signal', token.signal_keyword, iToken, lObjects)

    iCurrent = identifier_list.classify_until([':'], iCurrent, lObjects, token.identifier)

    iCurrent = utils.assign_next_token_required(':', token.colon, iCurrent, lObjects)

    iCurrent = mode.classify(iCurrent, lObjects)

    iCurrent = subtype_indication.classify_until([';', 'bus', ':='], iCurrent, lObjects, token.subtype_indication)

    iCurrent = utils.assign_next_token_if('bus', token.bus_keyword, iCurrent, lObjects)

    if utils.is_next_token(':=', iCurrent, lObjects):

        iCurrent = utils.assign_next_token_required(':=', token.assignment, iCurrent, lObjects)

        iCurrent = expression.classify_until([')', ';'], iCurrent, lObjects)

    return iCurrent
