
from vsg.token import conditional_variable_assignment as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import conditional_expressions

'''
    conditional_variable_assignment ::=
        target := conditional_expressions ;
'''

def detect(iToken, lObjects):

    if utils.is_next_token('when', iToken, lObjects):
        return False
    if utils.find_in_range(':=', iToken, ';', lObjects):
        if not utils.find_in_range('with', iToken, ';', lObjects):
            if utils.find_in_range('when', iToken, ';', lObjects):
                return True
            return False
        return False
    return False


def classify(iToken, lObjects):

    iCurrent = utils.assign_tokens_until(':=', token.target, iToken, lObjects)
    iCurrent = utils.assign_next_token_required(':=', token.assignment, iCurrent, lObjects)

    iCurrent = conditional_expressions.classify_until([';'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
