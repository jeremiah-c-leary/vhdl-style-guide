
from vsg.token import assertion as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import condition
from vsg.vhdlFile.classify import expression


def classify(iToken, lObjects):
    '''
    assertion ::=
        assert condition
            [ report expression ]
            [ severity expression ]

    The key to detecting this is looking for the keyword **assert** before a semicolon.
    '''

    iCurrent = utils.assign_next_token_required('assert', token.keyword, iToken, lObjects)

    iCurrent = condition.classify_until(['report', 'severity', ';'], iCurrent, lObjects)

    if utils.is_next_token('report', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('report', token.report_keyword, iCurrent, lObjects)
        iCurrent = expression.classify_until(['severity', ';'], iCurrent, lObjects)

    if utils.is_next_token('severity', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('severity', token.severity_keyword, iCurrent, lObjects)
        iCurrent = expression.classify_until([';'], iCurrent, lObjects)

    return iCurrent
