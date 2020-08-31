
from vsg.token import delay_mechanism as token
from vsg.vhdlFile import utils


def tokenize(iStart, iEnd, lAllObjects):
    '''
    delay_mechanism ::=
        transport
      | [ reject *time*_expression ] inertial
    '''

    for iToken in range(iStart, iEnd):
        if utils.is_item(lAllObjects, iToken):
            if utils.object_value_is(lAllObjects, iToken, 'transport'):
                utils.assign_token(lAllObjects, iToken, token.transport_keyword)
                break
            if utils.object_value_is(lAllObjects, iToken, 'inertial'):
                utils.assign_token(lAllObjects, iToken, token.inertial_keyword)
                break
            if utils.object_value_is(lAllObjects, iToken, 'reject'):
                utils.assign_token(lAllObjects, iToken, token.reject_keyword)

