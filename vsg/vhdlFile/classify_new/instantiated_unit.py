
from vsg.token import instantiated_unit as token

from vsg.vhdlFile import utils


def detect(iCurrent, lObjects):
    '''
    instantiated_unit ::=
        [ component ] component_name
      | entity entity_name [ ( *architecture*_identifier ) ]
      | configuration configuration_name
    '''
    iToken = iCurrent
    if utils.is_next_token_one_of(['component', 'entity', 'configuration'], iToken, lObjects):
        return True
    if utils.find_in_next_n_tokens(';', 2, iToken, lObjects):
        return True
    # Check if this is a signal assignment
    if utils.find_in_range('<=', iToken, ';', lObjects):
        return False
    if utils.find_in_range('generate', iToken, ';', lObjects):
        return False
    return True

def classify(iToken, lObjects):

    iCurrent = iToken

    if utils.is_next_token('component', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('component', token.component_keyword, iCurrent, lObjects)
        iCurrent = utils.assign_next_token(token.component_name, iCurrent, lObjects)

    elif utils.is_next_token('configuration', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('configuration', token.configuration_keyword, iCurrent, lObjects)
        iCurrent = utils.assign_next_token(token.configuration_name, iCurrent, lObjects)

    elif utils.is_next_token('entity', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('entity', token.entity_keyword, iCurrent, lObjects)
        iCurrent = utils.assign_next_token(token.entity_name, iCurrent, lObjects)

        if utils.is_next_token('(', iCurrent, lObjects):
            iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iCurrent, lObjects)
            iCurrent = utils.assign_next_token_if_not(')', token.architecture_identifier, iCurrent, lObjects)
            iCurrent = utils.assign_next_token_required(')', token.close_parenthesis, iCurrent, lObjects)
    else:
        iCurrent = utils.assign_next_token(token.component_name, iCurrent, lObjects)

    return iCurrent

