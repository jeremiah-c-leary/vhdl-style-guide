
from vsg import parser

from vsg.token import conditional_expressions as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import condition
from vsg.vhdlFile.classify_new import expression


'''
    conditional_expressions ::=
        expression when condition
        { else expression when condition }
        [ else expression ]
'''


def classify_until(lUntils, iToken, lObjects):

    lMyElseUntils = lUntils.copy()
    lMyElseUntils.append('else')
    lMyWhenUntils = lUntils.copy()
    lMyWhenUntils.append('when')

    iCurrent = expression.classify_until('when', iToken, lObjects)
    iCurrent = utils.assign_next_token_required('when', token.when_keyword, iCurrent, lObjects)
    iCurrent = condition.classify_until(lMyElseUntils, iCurrent, lObjects)

    while utils.is_next_token('else', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('else', token.else_keyword, iCurrent, lObjects)
        iCurrent = expression.classify_until(lMyWhenUntils, iCurrent, lObjects)
        if lObjects[iCurrent].get_value() in lUntils:
            break
        iCurrent = utils.assign_next_token_required('when', token.when_keyword, iCurrent, lObjects)
        iCurrent = condition.classify_until(lMyElseUntils, iCurrent, lObjects)

    return iCurrent
