
from vsg.token import port_map_aspect as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import association_list


def detect(iToken, lObjects):
    '''
    port_map_aspect ::=
        port map ( *port*_association_list )
    '''

    if utils.are_next_consecutive_tokens(['port', 'map', '('], iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('port', token.port_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('map', token.map_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iCurrent, lObjects)

    iCurrent = association_list.classify(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(')', token.close_parenthesis, iCurrent, lObjects)

    return iCurrent
