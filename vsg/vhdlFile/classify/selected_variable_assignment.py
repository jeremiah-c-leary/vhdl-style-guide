
from vsg.token import selected_variable_assignment as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import expression
from vsg.vhdlFile.classify import selected_expressions


def detect(iToken, lObjects):
    '''
    selected_variable_assignment ::=
        with expression select [ ? ]
           target := selected_expressions ;
    '''

    if utils.is_next_token_one_of(['when', 'if', 'elsif', 'else'], iToken, lObjects):
        return False
    if utils.find_in_range(':=', iToken, ';', lObjects):
        if utils.find_in_range('with', iToken, ';', lObjects):
            return True
        return False
    return False


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('with', token.with_keyword, iToken, lObjects)

    iCurrent = expression.classify_until(['select'], iToken, lObjects)

    iCurrent = utils.assign_next_token_required('select', token.select_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if('?', token.question_mark, iCurrent, lObjects)
    iCurrent = utils.assign_tokens_until(':=', token.target, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(':=', token.assignment, iCurrent, lObjects)

    iCurrent = selected_expressions.classify_until([';'], iToken, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
