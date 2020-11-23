
from vsg.token import selected_expressions as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import choices
from vsg.vhdlFile.classify import expression


def classify_until(lUntils, iToken, lObjects):
    '''
    selected_expressions ::=
        { expression when choices , }
        expression when choices
    '''

    iCurrent = iToken
    lMyUntils = lUntils
    lMyUntils.append(',')

    iCurrent = expression.classify_until(['when'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('when', token.when_keyword, iCurrent, lObjects)

    iCurrent = choices.classify_until(lMyUntils, iCurrent, lObjects)

    while utils.is_next_token(',', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required(',', token.comma, iCurrent, lObjects)

        iCurrent = expression.classify_until(['when'], iCurrent, lObjects)

        iCurrent = utils.assign_next_token_required('when', token.when_keyword, iCurrent, lObjects)

        iCurrent = choices.classify_until(lMyUntils, iCurrent, lObjects)

    return iCurrent
