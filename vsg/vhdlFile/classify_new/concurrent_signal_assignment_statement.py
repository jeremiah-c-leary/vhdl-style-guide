
from vsg.token import concurrent_signal_assignment_statement as token

from vsg import parser

from vsg.vhdlFile.classify_new import concurrent_simple_signal_assignment
from vsg.vhdlFile.classify_new import concurrent_conditional_signal_assignment
from vsg.vhdlFile.classify_new import concurrent_selected_signal_assignment

from vsg.vhdlFile import utils


def detected(iObject, oObject, lAllObjects, lNewObjects, dVars):
    '''
    concurrent_signal_assignment_statement ::=
        [ label : ] [ postponed ] concurrent_simple_signal_assignment
      | [ label : ] [ postponed ] concurrent_conditional_signal_assignment
      | [ label : ] [ postponed ] concurrent_selected_signal_assignment
    '''

    if concurrent_selected_signal_assignment.detected(iObject, oObject, lAllObjects, lNewObjects, dVars):
        iNewIndex = tokenize_label(iObject, oObject, lAllObjects, lNewObjects, dVars)
        iNewIndex = tokenize_postponed(iNewIndex, oObject, lAllObjects, lNewObjects, dVars)
        concurrent_selected_signal_assignment.tokenize(iNewIndex, oObject, lAllObjects, lNewObjects, dVars)
        lNewObjects.append(lAllObjects[iObject])
        return True

    elif concurrent_conditional_signal_assignment.detected(iObject, oObject, lAllObjects, lNewObjects, dVars):
        iNewIndex = tokenize_label(iObject, oObject, lAllObjects, lNewObjects, dVars)
        iNewIndex = tokenize_postponed(iNewIndex, oObject, lAllObjects, lNewObjects, dVars)
        concurrent_conditional_signal_assignment.tokenize(iNewIndex, oObject, lAllObjects, lNewObjects, dVars)
        lNewObjects.append(lAllObjects[iObject])
        return True

    elif concurrent_simple_signal_assignment.detected(iObject, oObject, lAllObjects, lNewObjects, dVars):
        iNewIndex = tokenize_label(iObject, oObject, lAllObjects, lNewObjects, dVars)
        iNewIndex = tokenize_postponed(iNewIndex, oObject, lAllObjects, lNewObjects, dVars)
        concurrent_simple_signal_assignment.tokenize(iNewIndex, oObject, lAllObjects, lNewObjects, dVars)
        lNewObjects.append(lAllObjects[iObject])
        return True

    return False


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
    iIndex = iObject
    iItemCount = 0
    if has_label(iObject, oObject, lAllObjects, lNewObjects, dVars):
        while iItemCount < 2:
            if utils.is_item(lAllObjects, iIndex):
                if iItemCount == 0:
                    utils.assign_token(lAllObjects, iIndex, token.label_name) 
                if iItemCount == 1:
                    utils.assign_token(lAllObjects, iIndex, token.label_colon) 
                iItemCount += 1
            iIndex += 1
    return iIndex


def tokenize_postponed(iObject, oObject, lAllObjects, lNewObjects, dVars):
    iIndex = iObject
    iItemCount = 0
    while iItemCount < 3:
        if utils.is_item(lAllObjects, iIndex):
            if utils.object_value_is(lAllObjects, iIndex, 'postponed'):
                utils.assign_token(lAllObjects, iIndex, token.postponed_keyword) 
                return iIndex
            iItemCount += 1
        iIndex += 1
    return iObject
