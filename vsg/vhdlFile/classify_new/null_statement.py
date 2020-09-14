
from vsg.token import null_statement as token

from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    '''
    null_statement ::=
        [ label : ] null ;
    '''
    if utils.are_next_consecutive_tokens([None, ':', 'null'], iToken, lObjects):
        return classify(iToken, lObjects)
    if utils.is_next_token('null', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.tokenize_label(iToken, lObjects, token.label, token.label_colon)
    iCurrent = utils.assign_next_token_required('null', token.null_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
