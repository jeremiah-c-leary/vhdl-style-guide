
from vsg.token import selected_waveform_assignment as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import delay_mechanism
from vsg.vhdlFile.classify import expression
from vsg.vhdlFile.classify import selected_waveforms


def detect(iToken, lObjects):
    '''
    selected_waveform_assignment ::=
        with expression select [ ? ]
            target <= [delay_machanism] selected_waveforms ;
    '''

    if utils.is_next_token_one_of(['when', 'if', 'elsif', 'else'], iToken, lObjects):
        return False
    if utils.find_in_range('<=', iToken, ';', lObjects):
        if not utils.find_in_range('force', iToken, ';', lObjects):
            return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('with', token.with_keyword, iToken, lObjects)
    iCurrent = expression.classify_until(['select'], iToken, lObjects)
    iCurrent = utils.assign_next_token_required('select', token.select_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if('?', token.question_mark, iCurrent, lObjects)
    iCurrent = utils.assign_tokens_until('<=', token.target, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('<=', token.assignment, iCurrent, lObjects)

    iCurrent = delay_mechanism.detect(iCurrent, lObjects)

    iCurrent = selected_waveforms.classify_until([';'], iToken, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
