
from vsg.token import port_clause as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import port_list

'''
    port_clause ::=
        port ( port_list ) ;
'''


def detect(iToken, lObjects):
    iCurrent = utils.find_next_token(iToken, lObjects)
    if utils.object_value_is(lObjects, iCurrent, 'port'):
        iCurrent = utils.increment_token_count(iCurrent)
        if utils.is_next_token('(', iCurrent, lObjects):
            return classify(iToken, lObjects)
        else:
            return iToken
    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required('port', token.port_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iCurrent, lObjects)
    iCurrent = port_list.classify(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(')', token.close_parenthesis, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)
    return iCurrent

