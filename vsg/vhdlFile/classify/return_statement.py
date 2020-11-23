
from vsg.token import return_statement as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import expression


def detect(iToken, lObjects):
    '''
    return_statement ::=
        [ label : ] return [ expression ] ;
    '''

    if utils.find_in_next_n_tokens(':', 2, iToken, lObjects):
        if utils.find_in_next_n_tokens('return', 3, iToken, lObjects):
            return classify(iToken, lObjects)
    if utils.is_next_token('return', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.tokenize_label(iToken, lObjects, token.label, token.label_colon)
    iCurrent = utils.assign_next_token_required('return', token.return_keyword, iCurrent, lObjects)
    if not utils.is_next_token(';', iCurrent, lObjects):
        iCurrent = expression.classify_until([';'], iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
