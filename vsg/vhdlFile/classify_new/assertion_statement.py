
from vsg.token import assertion_statement as token

from vsg.vhdlFile.classify_new import assertion

from vsg.vhdlFile import utils

'''
    assertion_statement ::=
        [ label : ] assertion ;
'''

def detect(iToken, lObjects):
    if utils.keyword_found('assert', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.tokenize_label(iToken, lObjects, token.label, token.label_colon)
    iCurrent = assertion.classify(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
