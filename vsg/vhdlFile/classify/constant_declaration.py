
from vsg.token import constant_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import expression
from vsg.vhdlFile.classify import identifier_list
from vsg.vhdlFile.classify import subtype_indication


def detect(iToken, lObjects):
    '''
    constant_declaration ::=
        constant identifier_list : subtype_indication [ := expression ] ;
    '''

    if utils.is_next_token('constant', iToken, lObjects):
        return classify(iToken, lObjects)

    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('constant', token.constant_keyword, iToken, lObjects)

    iCurrent = identifier_list.classify_until([':'], iCurrent, lObjects, token.identifier)

    iCurrent = utils.assign_next_token_required(':', token.colon, iCurrent, lObjects)

    iCurrent = subtype_indication.classify(iCurrent, lObjects)

    if utils.is_next_token(':=', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required(':=', token.assignment_operator, iCurrent, lObjects)

        iCurrent = expression.classify_until([';'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
