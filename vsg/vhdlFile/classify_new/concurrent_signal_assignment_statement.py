
from vsg.token import concurrent_signal_assignment_statement as token

from vsg import parser

from vsg.vhdlFile.classify_new import concurrent_simple_signal_assignment
from vsg.vhdlFile.classify_new import concurrent_conditional_signal_assignment
from vsg.vhdlFile.classify_new import concurrent_selected_signal_assignment

from vsg.vhdlFile import utils


def detect(iCurrent, lObjects):
    '''
    concurrent_signal_assignment_statement ::=
        [ label : ] [ postponed ] concurrent_simple_signal_assignment
      | [ label : ] [ postponed ] concurrent_conditional_signal_assignment
      | [ label : ] [ postponed ] concurrent_selected_signal_assignment
    '''
    iReturn = iCurrent
    if concurrent_selected_signal_assignment.detect(iCurrent, lObjects):
        iReturn = utils.tokenize_label(iReturn, lObjects, token.label_name, token.label_colon)
        iReturn = utils.tokenize_postponed(iReturn, lObjects, token.postponed_keyword)
        iReturn = concurrent_selected_signal_assignment.classify(iReturn, lObjects)

    elif concurrent_conditional_signal_assignment.detect(iCurrent, lObjects):
        iReturn = utils.tokenize_label(iReturn, lObjects, token.label_name, token.label_colon)
        iReturn = utils.tokenize_postponed(iReturn, lObjects, token.postponed_keyword)
        iReturn = concurrent_conditional_signal_assignment.classify(iReturn, lObjects)

    elif concurrent_simple_signal_assignment.detect(iCurrent, lObjects):
        iReturn = utils.tokenize_label(iReturn, lObjects, token.label_name, token.label_colon)
        iReturn = utils.tokenize_postponed(iReturn, lObjects, token.postponed_keyword)
        iReturn = concurrent_simple_signal_assignment.classify(iReturn, lObjects)

    return iReturn
