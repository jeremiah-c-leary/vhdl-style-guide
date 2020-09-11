
from vsg.token import timeout_clause as token

from vsg.vhdlFile.classify_new import expression

from vsg.vhdlFile import utils

'''
    timeout_clause ::=
        for *time*_expression
'''

def detect(iToken, lObjects):
    if utils.is_next_token('for', iToken, lObjects):
        return True
    return False


def classify_until(lUntils, iToken, lObjects):

    iCurrent = utils.assign_next_token_required('for', token.for_keyword, iToken, lObjects)

    iCurrent = expression.classify_until(lUntils, iCurrent, lObjects)

    return iCurrent
