
from vsg.token import concurrent_signal_assignment_statement as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import concurrent_conditional_signal_assignment
from vsg.vhdlFile.classify import concurrent_selected_signal_assignment
from vsg.vhdlFile.classify import concurrent_simple_signal_assignment


def detect(iToken, lObjects):
    '''
    concurrent_signal_assignment_statement ::=
        [ label : ] [ postponed ] concurrent_simple_signal_assignment
      | [ label : ] [ postponed ] concurrent_conditional_signal_assignment
      | [ label : ] [ postponed ] concurrent_selected_signal_assignment
    '''

    iCurrent = iToken
    if concurrent_selected_signal_assignment.detect(iToken, lObjects):
        iCurrent = utils.tokenize_label(iCurrent, lObjects, token.label_name, token.label_colon)
        iCurrent = utils.tokenize_postponed(iCurrent, lObjects, token.postponed_keyword)
        iCurrent = concurrent_selected_signal_assignment.classify(iCurrent, lObjects)

    elif concurrent_conditional_signal_assignment.detect(iToken, lObjects):
        iCurrent = utils.tokenize_label(iCurrent, lObjects, token.label_name, token.label_colon)
        iCurrent = utils.tokenize_postponed(iCurrent, lObjects, token.postponed_keyword)
        iCurrent = concurrent_conditional_signal_assignment.classify(iCurrent, lObjects)

    elif concurrent_simple_signal_assignment.detect(iToken, lObjects):
        iCurrent = utils.tokenize_label(iCurrent, lObjects, token.label_name, token.label_colon)
        iCurrent = utils.tokenize_postponed(iCurrent, lObjects, token.postponed_keyword)
        iCurrent = concurrent_simple_signal_assignment.classify(iCurrent, lObjects)

    return iCurrent
