
from vsg.token import delay_mechanism as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import expression


def detect(iToken, lObjects):
    '''
    delay_mechanism ::=
        transport
      | [ reject *time*_expression ] inertial
    '''
    if utils.is_next_token_one_of(['transport', 'reject', 'inertial'], iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    if utils.is_next_token('transport', iToken, lObjects):

        return utils.assign_next_token_required('transport', token.transport_keyword, iToken, lObjects)

    else:

        iCurrent = iToken

        if utils.is_next_token('reject', iCurrent, lObjects):
            iCurrent = utils.assign_next_token_required('reject', token.reject_keyword, iCurrent, lObjects)
            iCurrent = expression.classify_until(['inertial'], iCurrent, lObjects)

        iCurrent = utils.assign_next_token_required('inertial', token.inertial_keyword, iCurrent, lObjects)
        return iCurrent
