
from vsg.token import simple_variable_assignment as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import expression

'''
    simple_variable_assignment ::=
        target := expression ;
'''

def detect(iToken, lObjects):

    if utils.find_in_range(':=', iToken, ';', lObjects):
        if utils.find_in_range('with', iToken, ';', lObjects):
            return False
        if utils.find_in_range('when', iToken, ';', lObjects):
            return False
        return True
    return False


def classify(iToken, lObjects):

    iCurrent = utils.assign_tokens_until(':=', token.target, iToken, lObjects)
    iCurrent = utils.assign_next_token_required(':=', token.assignment, iCurrent, lObjects)

    iCurrent = expression.classify_until([';'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
