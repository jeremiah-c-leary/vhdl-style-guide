
from vsg.token import context_reference as token

from vsg.vhdlFile import utils


def detect(iCurrent, lObjects):
    '''
    context_reference ::=
        context selected_name { , selected_name } ;
    '''
    if utils.object_value_is(lObjects, iCurrent, 'context'):
        if not utils.find_in_range('is', iCurrent, ';', lObjects):
            return classify(iCurrent, lObjects)
    return iCurrent


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('context', token.keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token(token.selected_name, iCurrent, lObjects)
    while utils.is_next_token(',', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required(',', token.comma, iCurrent, lObjects)
        iCurrent = utils.assign_next_token(token.selected_name, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)
    return iCurrent
