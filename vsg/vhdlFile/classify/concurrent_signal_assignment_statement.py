
from vsg.token import concurrent_signal_assignment_statement as token

from vsg.vhdlFile.classify import concurrent_simple_signal_assignment
from vsg.vhdlFile.classify import concurrent_conditional_signal_assignment


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    concurrent_signal_assignment_statement ::=
        [ label : ] [ postponed ] concurrent_simple_signal_assignment
      | [ label : ] [ postponed ] concurrent_conditional_signal_assignment
      | [ label : ] [ postponed ] concurrent_selected_signal_assignment
    '''

    if classify_postponed_keyword(oObject, iObject, lObjects, dVars):
        return True

    if concurrent_conditional_signal_assignment.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if concurrent_simple_signal_assignment.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def classify_postponed_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'postponed':
        lObjects[iObject] = token.postposed_keyword(sValue)


def clear_flags(dVars):
    concurrent_simple_signal_assignment.clear_flags(dVars)
