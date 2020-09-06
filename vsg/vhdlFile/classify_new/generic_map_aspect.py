
from vsg.token import generic_map_aspect as token

from vsg.vhdlFile import utils
from vsg.vhdlFile.classify_new import association_list


def detect(iToken, lObjects):
    '''
    generic_map_aspect ::=
        generic map ( *generic*_association_list )
    '''
    iCurrent = utils.find_next_token(iToken, lObjects)
    if utils.object_value_is(lObjects, iCurrent, 'generic'):
        return classify(iCurrent, lObjects)
    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_if('generic', token.generic_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if('map', token.map_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if('(', token.open_parenthesis, iCurrent, lObjects)
    iCurrent = association_list.classify(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if(')', token.close_parenthesis, iCurrent, lObjects)
    return iCurrent
