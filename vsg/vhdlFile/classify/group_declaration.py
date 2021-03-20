
from vsg.token import group_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import group_constituent_list


def detect(iToken, lObjects):
    '''
    group_declaration ::=
        group identifier : group_template_name ( group_constituent_list ) ;
    '''

    if utils.is_next_token('group', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('group', token.group_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token(token.identifier, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(':', token.colon, iCurrent, lObjects)
    iCurrent = utils.assign_next_token(token.group_template_name, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iCurrent, lObjects)
    iCurrent = group_constituent_list.classify(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(')', token.close_parenthesis, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
