
from vsg import parser

from vsg.token import selected_force_assignment as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import force_mode
from vsg.vhdlFile.classify_new import expression
from vsg.vhdlFile.classify_new import selected_expressions

'''
    selected_force_assignment ::= [§ 10.5.4]
        with expression select [ ? ]
            target <= force [ force_mode ] selected_expressions ;
'''

def detect(iToken, lObjects):

    if utils.is_next_token('when', iToken, lObjects):
        return False
    if utils.find_in_range('<=', iToken, ';', lObjects):
        if utils.find_in_range('force', iToken, ';', lObjects):
            return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('with', token.with_keyword, iToken, lObjects)
    iCurrent = expression.classify_until('select', iToken, lObjects)
    iCurrent = utils.assign_next_token_required('select', token.select_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if('?', token.question_mark, iCurrent, lObjects)
    iCurrent = utils.assign_tokens_until('<=', token.target, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('<=', token.assignment, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('force', token.force_keyword, iCurrent, lObjects)

    iCurrent = force_mode.detect(iCurrent, lObjects)

    iCurrent = selected_expressions.classify_until([';'], iToken, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
