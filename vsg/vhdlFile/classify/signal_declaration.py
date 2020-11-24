
from vsg.token import signal_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import expression
from vsg.vhdlFile.classify import identifier_list
from vsg.vhdlFile.classify import signal_kind
from vsg.vhdlFile.classify import subtype_indication


def detect(iToken, lObjects):
    '''
    signal_declaration ::=
        signal identifier_list : subtype_indication [ signal_kind ] [ := expression ] ;
    '''

    if utils.is_next_token('signal', iToken, lObjects):
        return classify(iToken, lObjects)

    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('signal', token.signal_keyword, iToken, lObjects)
    iCurrent = identifier_list.classify_until([':'], iCurrent, lObjects, token.identifier)
    iCurrent = utils.assign_next_token_required(':', token.colon, iCurrent, lObjects)

    iCurrent = subtype_indication.classify_until([';', ':=', 'bus', 'register'], iCurrent, lObjects)

    iCurrent = signal_kind.detect(iToken, lObjects)

    if utils.is_next_token(':=', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required(':=', token.assignment_operator, iCurrent, lObjects)
        iCurrent = expression.classify_until([';'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
