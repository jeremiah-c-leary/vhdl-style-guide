
from vsg.token import next_statement as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import condition


def detect(iToken, lObjects):
    '''
    next_statement ::=
        [ label : ] next [ loop_label ] [ when condition ] ;
    '''
    if utils.are_next_consecutive_tokens([None, ':', 'next'], iToken, lObjects):
        return classify(iToken, lObjects)
    if utils.is_next_token('next', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.tokenize_label(iToken, lObjects, token.label, token.label_colon)
    iCurrent = utils.assign_next_token_required('next', token.next_keyword, iCurrent, lObjects)

    if not utils.is_next_token(';', iCurrent, lObjects) and not utils.is_next_token('when', iCurrent, lObjects):
        iCurrent = utils.assign_next_token(token.loop_label, iCurrent, lObjects)

    if utils.is_next_token('when', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('when', token.when_keyword, iCurrent, lObjects)
        iCurrent = condition.classify_until([';'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
