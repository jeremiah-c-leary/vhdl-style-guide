
from vsg.token import timeout_clause as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import expression



def detect(iToken, lObjects):
    '''
    timeout_clause ::=
        for *time*_expression
    '''

    if utils.is_next_token('for', iToken, lObjects):
        return True
    return False


def classify_until(lUntils, iToken, lObjects):

    iCurrent = utils.assign_next_token_required('for', token.for_keyword, iToken, lObjects)

    iCurrent = expression.classify_until(lUntils, iCurrent, lObjects)

    return iCurrent
