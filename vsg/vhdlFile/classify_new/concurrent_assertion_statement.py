
from vsg.token import concurrent_assertion_statement as token

from vsg import parser

from vsg.vhdlFile.classify_new import assertion

from vsg.vhdlFile import utils

'''
    concurrent_assertion_statement ::=
        [ label : ] [ postponed ] assertion ;
'''


def detect(iCurrent, lObjects):
    '''
    concurrent_assertion_statement ::=
        [ label : ] [ postponed ] assertion ;
    '''

    if assertion.detect(iCurrent, lObjects):
        return classify(iCurrent, lObjects)
    return iCurrent


def classify(iCurrent, lObjects):
    iReturn = iCurrent
    iReturn = tokenize_label(iReturn, lObjects)
    iReturn = tokenize_postponed(iReturn, lObjects)
    iReturn = assertion.tokenize(iReturn, lObjects)
    iReturn = tokenize_semicolon(iReturn, lObjects)
    return iReturn


def has_label(iObject, lObjects):
    iItemCount = 0
    iIndex = iObject
    try:
        while iItemCount < 2:
            if type(lObjects[iIndex]) == parser.item:
                iItemCount += 1
            iIndex += 1
        else:
            if lObjects[iIndex-1].get_value().lower() == ':':
                return True
    except IndexError:
        return False
    return False
    

def tokenize_label(iCurrent, lObjects):
    iIndex = iCurrent
    iItemCount = 0
    if has_label(iCurrent, lObjects):
        while iItemCount < 2:
            if utils.is_item(lObjects, iIndex):
                if iItemCount == 0:
                    utils.assign_token(lObjects, iIndex, token.label_name) 
                if iItemCount == 1:
                    utils.assign_token(lObjects, iIndex, token.label_colon) 
                iItemCount += 1
            iIndex += 1
    return iIndex


def tokenize_postponed(iObject, lObjects):
    iIndex = iObject
    iItemCount = 0
    while iItemCount < 3:
        if utils.is_item(lObjects, iIndex):
            if utils.object_value_is(lObjects, iIndex, 'postponed'):
                utils.assign_token(lObjects, iIndex, token.postponed_keyword) 
                return iIndex
            iItemCount += 1
        iIndex += 1
    return iObject


def tokenize_semicolon(iObject, lObjects):
    iIndex = iObject
    iItemCount = 0
    while iItemCount < 3:
        if utils.is_item(lObjects, iIndex):
            if utils.object_value_is(lObjects, iIndex, ';'):
                utils.assign_token(lObjects, iIndex, token.semicolon) 
                return iIndex
            iItemCount += 1
        iIndex += 1
    return iObject
