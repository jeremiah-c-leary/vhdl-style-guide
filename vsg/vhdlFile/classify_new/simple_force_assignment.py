
from vsg.token import simple_force_assignment as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import expression
from vsg.vhdlFile.classify_new import force_mode

'''
    simple_force_assignment ::=
        target <= force [ force_mode ] expression ;
'''

def detect(iToken, lObjects):

    if utils.find_in_range('force', iToken, ';', lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_tokens_until('<=', token.target, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('<=', token.assignment, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('force', token.force_keyword, iCurrent, lObjects)

    iCurrent = force_mode.detect(iCurrent, lObjects)
    iCurrent = expression.classify_until([';'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
