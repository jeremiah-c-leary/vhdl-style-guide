
from vsg.token import signal_assignment_statement as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import conditional_signal_assignment
from vsg.vhdlFile.classify import selected_signal_assignment
from vsg.vhdlFile.classify import simple_signal_assignment


def detect(iToken, lObjects):
    '''
    signal_assignment_statement ::=
        [ label : ] simple_signal_assignment
      | [ label : ] conditional_signal_assignment
      | [ label : ] selected_signal_assignment
    '''

    iCurrent = iToken

    if selected_signal_assignment.detect(iToken, lObjects):
        iCurrent = utils.tokenize_label(iCurrent, lObjects, token.label, token.label_colon)
        iCurrent = selected_signal_assignment.classify(iCurrent, lObjects)

    elif conditional_signal_assignment.detect(iToken, lObjects):
        iCurrent = utils.tokenize_label(iCurrent, lObjects, token.label, token.label_colon)
        iCurrent = conditional_signal_assignment.classify(iCurrent, lObjects)

    elif simple_signal_assignment.detect(iToken, lObjects):
        iCurrent = utils.tokenize_label(iCurrent, lObjects, token.label, token.label_colon)
        iCurrent = simple_signal_assignment.classify(iCurrent, lObjects)

    return iCurrent
