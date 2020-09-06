
from vsg.token import generic_clause as token

from vsg.vhdlFile import utils
from vsg.vhdlFile.classify_new import generic_list


def detect(iToken, lObjects):
    '''
    generic_clause ::=
        generic ( generic_list ) ;
    '''
    iCurrent = utils.find_next_token(iToken, lObjects)
    if utils.object_value_is(lObjects, iCurrent, 'generic'):
        iCurrent += 1
        iCurrent = utils.find_next_token(iCurrent, lObjects)
        if utils.object_value_is(lObjects, iCurrent, '('):
            return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_if('generic', token.generic_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if('(', token.open_parenthesis, iCurrent, lObjects)
    iCurrent = generic_list.classify(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if(')', token.close_parenthesis, iCurrent, lObjects)
    return iCurrent


