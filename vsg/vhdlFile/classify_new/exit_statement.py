
from vsg.token import exit_statement as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import condition


def detect(iToken, lObjects):
    '''
    exit_statement ::=
        [ label : ] exit [ loop_label ] [ when condition ] ;
    '''
    if utils.find_in_next_n_tokens('exit', 3, iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.tokenize_label(iToken, lObjects, token.label, token.label_colon)
    iCurrent = utils.assign_next_token_required('exit', token.exit_keyword, iCurrent, lObjects)

    if not utils.is_next_token(';', iCurrent, lObjects) and not utils.is_next_token('when', iCurrent, lObjects):
        iCurrent = utils.assign_next_token(token.loop_label, iCurrent, lObjects)

    if utils.is_next_token('when', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('when', token.when_keyword, iCurrent, lObjects)
        iCurrent = condition.classify_until([';'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
