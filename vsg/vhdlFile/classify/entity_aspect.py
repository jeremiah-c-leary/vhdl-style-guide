
from vsg.token import entity_aspect as token

from vsg.vhdlFile import utils


def classify(iToken, lObjects):
    '''
    entity_aspect ::=
        **entity** entity_name [ ( architecture_identifier ) ]
      | **configuration** configuration_name
      | **open**
    '''
    iCurrent = iToken

    if utils.is_next_token('open', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('open', token.open_keyword, iCurrent, lObjects)

    elif utils.is_next_token('configuration', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('configuration', token.configuration_keyword, iCurrent, lObjects)
        iCurrent = utils.assign_next_token(token.configuration_name, iCurrent, lObjects)

    elif utils.is_next_token('entity', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('entity', token.entity_keyword, iCurrent, lObjects)
        iCurrent = utils.assign_next_token(token.entity_name, iCurrent, lObjects)

        if utils.is_next_token('(', iCurrent, lObjects):
            iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iCurrent, lObjects)
            iCurrent = utils.assign_next_token(token.architecture_identifier, iCurrent, lObjects)
            iCurrent = utils.assign_next_token_required(')', token.close_parenthesis, iCurrent, lObjects)

    return iCurrent
