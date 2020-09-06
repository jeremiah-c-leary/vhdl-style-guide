
from vsg.vhdlFile.classify_new import generic_map_aspect

from vsg.token import interface_package_generic_map_aspect as token

from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    '''
    interface_package_generic_map_aspect ::=
        generic_map_aspect
      | generic map ( <> )
      | generic map ( default )
    '''
    iTokenCount = 0
    iCurrent = iToken
    while iTokenCount < 5:
        iCurrent = utils.find_next_token(iCurrent, lObjects)
        iTokenCount += 1
        if utils.object_value_is(lObjects, iCurrent, 'default'):
            return classify(iToken, lObjects)
        elif utils.object_value_is(lObjects, iCurrent, '<>'):
            return classify(iToken, lObjects)
        iCurrent += 1
    else:
        return generic_map_aspect.classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_if('generic', token.generic_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if('map', token.map_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if('(', token.open_parenthesis, iToken, lObjects)
    iCurrent = utils.assign_next_token_if('default', token.default_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if('<>', token.undefined_range, iToken, lObjects)
    iCurrent = utils.assign_next_token_if(')', token.close_parenthesis, iToken, lObjects)
    return iCurrent
