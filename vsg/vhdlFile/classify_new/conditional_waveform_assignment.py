
from vsg.token import conditional_waveform_assignment as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import delay_mechanism
from vsg.vhdlFile.classify_new import conditional_waveforms

'''
    conditional_waveform_assignment ::=
        target <= [ delay_mechanism ] conditional_waveforms ;
'''

def detect(iToken, lObjects):

    if not utils.find_in_range('force', iToken, ';', lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_tokens_until('<=', token.target, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('<=', token.assignment, iCurrent, lObjects)

    iCurrent = delay_mechanism.detect(iCurrent, lObjects)

    iCurrent = conditional_waveforms.classify_until([';'], iToken, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent
