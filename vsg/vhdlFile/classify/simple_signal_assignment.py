
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import simple_force_assignment
from vsg.vhdlFile.classify import simple_release_assignment
from vsg.vhdlFile.classify import simple_waveform_assignment


def detect(iToken, lObjects):
    '''
    simple_signal_assignment ::=
        simple_waveform_assignment
      | simple_force_assignment
      | simple_release_assignment
    '''

    if utils.find_in_next_n_tokens('if', 3, iToken, lObjects):
        return False
    if utils.find_in_range('<=', iToken, ';', lObjects):
        if utils.find_in_range('when', iToken, ';', lObjects):
            return False
        if utils.find_in_range('with', iToken, ';', lObjects):
            return False
        return True
    return False


def classify(iToken, lObjects):

    iCurrent = iToken
    iCurrent = simple_force_assignment.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = simple_release_assignment.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = simple_waveform_assignment.detect(iToken, lObjects)

    return iCurrent
