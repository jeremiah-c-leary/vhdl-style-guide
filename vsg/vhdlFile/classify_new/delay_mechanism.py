
from vsg.token import delay_mechanism as token
from vsg import parser
from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    if utils.is_next_token('transport', iToken, lObjects):
        return classify(iToken, lObjects)
    if utils.is_next_token('reject', iToken, lObjects):
        return classify(iToken, lObjects)
    if utils.is_next_token('inertial', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):
    '''
    delay_mechanism ::=
        transport
      | [ reject *time*_expression ] inertial
    '''
    if utils.is_next_token('transport', iToken, lObjects):
        return utils.assign_next_token_required('transport', token.transport_keyword, iToken, lObjects)
    else:
        iCurrent = iToken
        if utils.is_next_token('reject', iToken, lObjects):
            iCurrent = utils.assign_next_token_required('reject', token.reject_keyword, iCurrent, lObjects)
            iCurrent = utils.assign_tokens_until('inertial', parser.todo, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required('inertial', token.inertial_keyword, iCurrent, lObjects)
        return iCurrent
