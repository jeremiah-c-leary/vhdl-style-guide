
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import selected_waveform_assignment
from vsg.vhdlFile.classify_new import selected_force_assignment

'''
    selected_signal_assignment ::=
        selected_waveform_assignment
      | selected_force_assignment
'''

def detect(iToken, lObjects):
    if utils.find_in_range('<=', iToken, ';', lObjects):
        if utils.find_in_next_n_tokens('with', 3, iToken, lObjects):
            return True
    return False


def classify(iToken, lObjects):
    iCurrent = selected_waveform_assignment.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent    

    iCurrent = selected_force_assignment.detect(iToken, lObjects)

    return iCurrent
