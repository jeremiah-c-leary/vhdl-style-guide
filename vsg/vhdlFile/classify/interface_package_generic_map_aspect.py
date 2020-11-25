
from vsg.token import interface_package_generic_map_aspect as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import generic_map_aspect


def detect(iToken, lObjects):
    '''
    interface_package_generic_map_aspect ::=
        generic_map_aspect
      | generic map ( <> )
      | generic map ( default )
    '''
    if utils.are_next_consecutive_tokens(['generic', 'map', '(', '<>'], iToken, lObjects):
        return classify(iToken, lObjects)
    elif utils.are_next_consecutive_tokens(['generic', 'map', '(', 'default'], iToken, lObjects):
        return classify(iToken, lObjects)
    else:
       return generic_map_aspect.classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('generic', token.generic_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('map', token.map_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iToken, lObjects)
    iCurrent = utils.assign_next_token_if('default', token.default_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if('<>', token.undefined_range, iToken, lObjects)
    iCurrent = utils.assign_next_token_required(')', token.close_parenthesis, iToken, lObjects)

    return iCurrent
