
from vsg.token import variable_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import expression
from vsg.vhdlFile.classify import identifier_list
from vsg.vhdlFile.classify import subtype_indication


def detect(iToken, lObjects):
    '''
    variable_declaration ::=
        [ shared ] variable identifier_list : subtype_indication [ := expression ] ;
    '''

    if utils.is_next_token('shared', iToken, lObjects):
        return classify(iToken, lObjects)
    elif utils.is_next_token('variable', iToken, lObjects):
        return classify(iToken, lObjects)

    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_if('shared', token.shared_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('variable', token.variable_keyword, iCurrent, lObjects)

    iCurrent = identifier_list.classify_until([':'], iCurrent, lObjects, token.identifier)

    iCurrent = utils.assign_next_token_required(':', token.colon, iCurrent, lObjects)

    iCurrent = subtype_indication.classify_until([';', ':='], iCurrent, lObjects)

    if utils.is_next_token(':=', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required(':=', token.assignment_operator, iCurrent, lObjects)
        iCurrent = expression.classify_until([';'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)
    return iCurrent
