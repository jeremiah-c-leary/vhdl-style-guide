
from vsg.token import subprogram_header as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import generic_list
from vsg.vhdlFile.classify import generic_map_aspect


def detect(iToken, lObjects):
    '''
    subprogram_header ::=
        [ generic ( generic_list )
        [ generic_map_aspect ] ]
    '''

    if utils.is_next_token('generic', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    if utils.find_in_next_n_tokens('(', 2, iToken, lObjects):
        iCurrent = utils.assign_next_token_required('generic', token.generic_keyword, iToken, lObjects)
        iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iCurrent, lObjects)

        iCurrent = generic_list.classify(iCurrent, lObjects)

        iCurrent = utils.assign_next_token_required(')', token.close_parenthesis, iCurrent, lObjects)

    iCurrent = generic_map_aspect.detect(iToken, lObjects)

    return iCurrent
