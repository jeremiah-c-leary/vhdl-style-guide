
from vsg.token import concurrent_signal_assignment_statement as token

from vsg import parser

#from vsg.vhdlFile.classify import concurrent_simple_signal_assignment
from vsg.vhdlFile.classify_new import concurrent_conditional_signal_assignment
from vsg.vhdlFile.classify_new import concurrent_selected_signal_assignment

'''
    concurrent_signal_assignment_statement ::=
        [ label : ] [ postponed ] concurrent_simple_signal_assignment
      | [ label : ] [ postponed ] concurrent_conditional_signal_assignment
      | [ label : ] [ postponed ] concurrent_selected_signal_assignment
'''


def detected(iObject, oObject, lAllObjects, lNewObjects, dVars):
    '''
    concurrent_signal_assignment_statement ::=
        [ label : ] [ postponed ] concurrent_simple_signal_assignment
      | [ label : ] [ postponed ] concurrent_conditional_signal_assignment
      | [ label : ] [ postponed ] concurrent_selected_signal_assignment
    '''

    if concurrent_selected_signal_assignment.detected(iObject, oObject, lAllObjects, lNewObjects, dVars):
        tokenize_label(iObject, oObject, lAllObjects, lNewObjects, dVars)
        tokenize_postponed(iObject, oObject, lAllObjects, lNewObjects, dVars)
        concurrent_selected_signal_assignment.tokenize(iObject, oObject, lAllObjects, lNewObjects, dVars)
        lNewObjects.append(lAllObjects[iObject])
        return True

    elif concurrent_conditional_signal_assignment.detected(iObject, oObject, lAllObjects, lNewObjects, dVars):
        tokenize_label(iObject, oObject, lAllObjects, lNewObjects, dVars)
        tokenize_postponed(iObject, oObject, lAllObjects, lNewObjects, dVars)
        concurrent_conditional_signal_assignment.tokenize(iObject, oObject, lAllObjects, lNewObjects, dVars)
        lNewObjects.append(lAllObjects[iObject])
        return True



def has_label(iObject, oObject, lAllObjects, lNewObjects, dVars):
    iItemCount = 0
    iIndex = iObject
    try:
        while iItemCount < 2:
            if type(lAllObjects[iIndex]) == parser.item:
                iItemCount += 1
            iIndex += 1
        else:
            if lAllObjects[iIndex-1].get_value().lower() == ':':
                return True
    except IndexError:
        return False
    return False
    

def tokenize_label(iObject, oObject, lAllObjects, lNewObjects, dVars):
    if has_label(iObject, oObject, lAllObjects, lNewObjects, dVars):
        iIndex = iObject
        iItemCount = 0
        while iItemCount < 2:
            if type(lAllObjects[iIndex]) == parser.item:
                if iItemCount == 0:
                    lNewObjects.append(token.label_name(lAllObjects[iIndex].get_value()))
                if iItemCount == 1:
                    lNewObjects.append(token.label_colon(lAllObjects[iIndex].get_value()))
                iItemCount += 1
            iIndex += 1

def tokenize_postponed(iObject, oObject, lAllObjects, lNewObjects, dVars):
    iIndex = iObject
    iItemCount = 0
    while iItemCount < 3:
        if type(lAllObjects[iIndex]) == parser.item:
            if lAllObjects[iIndex].get_value().lower() == 'postponed':
                lNewObjects.append(token.postponed_keyword(lAllObjects[iIndex].get_value()))
            iItemCount += 1
        iIndex += 1
