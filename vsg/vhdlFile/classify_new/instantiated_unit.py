
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

    utils.find_next_token(iToken, lObjects)
    if utils.object_value_is(lObjects, iToken, 'component'):
        return True
    if utils.object_value_is(lObjects, iToken, 'entity'):
        return True
    if utils.object_value_is(lObjects, iToken, 'configuration'):
        return True
    # Check if this is a signal assignment
    if utils.find_in_range('<=', iToken, ';', lObjects):
        return False
    if utils.find_in_range('generate', iToken, ';', lObjects):
        return False
    return True

def classify(iToken, lObjects):
    iCurrent = utils.find_next_token(iToken, lObjects)
    if utils.object_value_is(lObjects, iCurrent, 'component'):
        iCurrent = utils.assign_token(lObjects, iCurrent, token.component_keyword)
        iCurrent = utils.assign_token(lObjects, iCurrent, token.component_name)
    elif utils.object_value_is(lObjects, iCurrent, 'configuration'):
        iCurrent = utils.assign_token(lObjects, iCurrent, token.configuration_keyword)
        iCurrent = utils.assign_token(lObjects, iCurrent, token.configuration_name)
    elif utils.object_value_is(lObjects, iCurrent, 'entity'):
        iCurrent = utils.assign_token(lObjects, iCurrent, token.entity_keyword)
        iCurrent = utils.assign_token(lObjects, iCurrent, token.entity_name)
        iCurrent = utils.find_next_token(iCurrent, lObjects)
        if utils.object_value_is(lObjects, iCurrent, '('):
            iCurrent = utils.assign_token(lObjects, iCurrent, token.open_parenthesis)
            iCurrent = utils.assign_token(lObjects, iCurrent, token.architecture_identifier)
            iCurrent = utils.assign_token(lObjects, iCurrent, token.close_parenthesis)
    else:
        iCurrent = utils.assign_token(lObjects, iCurrent, token.component_name)
    return iCurrent

