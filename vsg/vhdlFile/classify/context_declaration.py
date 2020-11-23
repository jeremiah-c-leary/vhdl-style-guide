
from vsg.token import context_declaration as token

from vsg.vhdlFile.classify import context_clause

from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    '''
    context_declaration ::=
        context identifier is
            context_clause
        end [ context ] [ context_simple_name ] ;
    '''

    iCurrent = utils.find_next_token(iToken, lObjects)
    if utils.object_value_is(lObjects, iCurrent, 'context'):
        if utils.find_in_range('is', iCurrent, ';', lObjects):
            return classify(iCurrent, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('context', token.context_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token(token.identifier, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('is', token.is_keyword, iCurrent, lObjects)

    iCurrent = context_clause.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if('context', token.end_context_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if_not(';', token.context_simple_name, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
