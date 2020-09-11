
from vsg.token import wait_statement as token

from vsg.vhdlFile.classify_new import sensitivity_clause
from vsg.vhdlFile.classify_new import condition_clause
from vsg.vhdlFile.classify_new import timeout_clause

from vsg.vhdlFile import utils

'''
    wait_statement ::=
        [ label : ] wait [ sensitivity_clause ] [ condition_clause ] [ timeout_clause ] ;
'''

def detect(iToken, lObjects):
    if utils.keyword_found('wait', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.tokenize_label(iToken, lObjects, token.label, token.label_colon)
    iCurrent = utils.assign_next_token_required('wait', token.wait_keyword, iCurrent, lObjects)

    if sensitivity_clause.detect(iCurrent, lObjects):
        iCurrent = sensitivity_clause.classify_until([';', 'for', 'until'], iCurrent, lObjects)

    if condition_clause.detect(iCurrent, lObjects):
        iCurrent = condition_clause.classify_until([';', 'for'], iCurrent, lObjects)

    if timeout_clause.detect(iCurrent, lObjects):
        iCurrent = timeout_clause.classify_until([';'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
