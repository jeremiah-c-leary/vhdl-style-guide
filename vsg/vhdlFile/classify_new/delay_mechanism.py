
from vsg.token import delay_mechanism as token
from vsg import parser
from vsg.vhdlFile import utils


def detect(iStart, iEnd, lObjects):
    for iToken in range(iStart, iEnd):
        if not utils.is_item(lObjects, iToken):
            continue
        if utils.object_value_is(lObjects, iToken, 'transport'):
            return classify(iStart, iEnd, lObjects)
        if utils.object_value_is(lObjects, iToken, 'inertial'):
            return classify(iStart, iEnd, lObjects)
    return iStart


def classify(iStart, iEnd, lObjects):
    '''
    delay_mechanism ::=
        transport
      | [ reject *time*_expression ] inertial
    '''

    for iToken in range(iStart, iEnd):
        if utils.is_item(lObjects, iToken):
            if utils.object_value_is(lObjects, iToken, 'transport'):
                utils.assign_token(lObjects, iToken, token.transport_keyword)
                return iToken
            if utils.object_value_is(lObjects, iToken, 'inertial'):
                utils.assign_token(lObjects, iToken, token.inertial_keyword)
                return iToken
            if utils.object_value_is(lObjects, iToken, 'reject'):
                utils.assign_token(lObjects, iToken, token.reject_keyword)
                continue
            utils.assign_token(lObjects, iToken, parser.todo)

    return iStart
