
from vsg.token import conditional_force_assignment as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import force_mode
from vsg.vhdlFile.classify import conditional_expressions


def detect(iToken, lObjects):
    '''
    conditional_force_assignment ::=
        target <= force [ force_mode ] conditional_expressions ;
    '''

    if utils.is_next_token_one_of(['when', 'if', 'elsif', 'else'], iToken, lObjects):
        return False
    if utils.find_in_range('<=', iToken, ';', lObjects):#
        if utils.find_in_range('force', iToken, ';', lObjects):
            return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_tokens_until('<=', token.target, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('<=', token.assignment, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('force', token.force_keyword, iCurrent, lObjects)

    iCurrent = force_mode.detect(iCurrent, lObjects)

    iCurrent = conditional_expressions.classify_until([';'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
