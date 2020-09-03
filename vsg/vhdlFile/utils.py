
from vsg import token
from vsg import parser


def is_object(sType, oType, oObject, lNewObjects):
    if oObject.get_value().lower() == sType:
        lNewObjects.append(oType(oObject.get_value()))
        return True
    return False


def is_current_level(dVars, sLevel):
    if current_level(dVars) == sLevel:
        return True
    return False

def pop_level(dVars):
    dVars['history'].pop()

def push_level(dVars, level):
    dVars['history'].append(level)

def current_level(dVars):
    return dVars['history'][-1]


def is_comment(oObject, lNewObjects):
    if type(oObject) == token.Comment:
        return True
    return False


def is_carriage_return(oObject, lNewObjects):
    if type(oObject) == token.CarriageReturn:
        return True
    return False


def is_blank_line(oObject, lNewObjects):
    if type(oObject) == token.BlankLine:
        return True
    return False


def is_whitespace(oObject, lNewObjects):
    if type(oObject) == token.Whitespace:
        return True
    return False

def have_guard_condition(iObject, lAllObjects):
    iItemCount = 0
    iIndex = iObject
    while iItemCount < 1:
        if type(lAllObjects[iIndex]) == parser.item:
            iItemCount += 1
            if lAllObjects[iIndex].get_value().lower() == '(':
                return True
        iIndex += 1
    return False

def have_is_keyword(iObject, lAllObjects):
    iItemCount = 0
    iIndex = iObject
    while iItemCount < 1:
        if type(lAllObjects[iIndex]) == parser.item:
            iItemCount += 1
            if lAllObjects[iIndex].get_value().lower() == 'is':
                return True
        iIndex += 1
    return False

def assign_token(lObjects, iToken, token):
    try:
        lObjects[iToken] = token(lObjects[iToken].get_value())
    except TypeError:
        lObjects[iToken] = token()

def object_value_is(lAllObjects, iToken, sString):
    if lAllObjects[iToken].get_value().lower() == sString.lower():
        return True
    return False

def is_item(lAllObjects, iToken):
    if type(lAllObjects[iToken]) == parser.item:
        return True
    return False

def get_bounds(lObjects, iStart, sEnd):
    iIndex = iStart
    while lObjects[iIndex].get_value() != sEnd:
        iIndex += 1
    else:
        iEnd = iIndex
        iStart = iStart
        iCurrent = iStart
    return iStart, iCurrent, iEnd

def get_range(lObjects, iStart, sEnd):
    iIndex = iStart
    while lObjects[iIndex].get_value() != sEnd:
#        print(lObjects[iIndex].get_value())
        iIndex += 1
    else:
        iEnd = iIndex
        iStart = iStart
    return iStart, iEnd

def classify_token(sToken, token, iToken, lObjects):
    if object_value_is(lObjects, iToken, sToken):
        assign_token(lObjects, iToken, token)
        return True
    return False


def find_in_range(sValue, iToken, sEnd, lObjects):
    iStart, iEnd = get_range(lObjects, iToken, sEnd)
    for iIndex in range(iStart, iEnd + 1):
        if object_value_is(lObjects, iIndex, sValue):
            return True
    return False


def find_next_token(iToken, lObjects):
    iReturn = iToken
    while not is_item(lObjects, iReturn):
        iReturn += 1
    return iReturn

def detect_submodule(iToken, lObjects, module):
    iLast = 0           
    iReturn = iToken
    while iLast != iReturn:
        iReturn = find_next_token(iReturn, lObjects)
        iLast = iReturn
        iReturn = module.detect(iReturn, lObjects)
    return iReturn

def classify_begin_keyword(iToken, token, lObjects):
    iReturn = iToken
    if classify_token('begin', token, iToken, lObjects):
        iReturn = iToken + 1
    return iReturn

def classify_is_keyword(iToken, token, lObjects):
    iReturn = iToken
    if classify_token('is', token, iToken, lObjects):
        iReturn = iToken + 1
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
    
def tokenize_postponed(iObject, lObjects, token):
    iIndex = iObject
    iItemCount = 0
    while iItemCount < 3:
        if is_item(lObjects, iIndex):
            if object_value_is(lObjects, iIndex, 'postponed'):
                assign_token(lObjects, iIndex, token) 
                return iIndex
            iItemCount += 1
        iIndex += 1
    return iObject

def tokenize_label(iCurrent, lObjects, label_token, colon_token):
    iIndex = iCurrent
    iItemCount = 0
    if has_label(iCurrent, lObjects):
        while iItemCount < 2:
            if is_item(lObjects, iIndex):
                if iItemCount == 0:
                    assign_token(lObjects, iIndex, label_token) 
                if iItemCount == 1:
                    assign_token(lObjects, iIndex, colon_token) 
                iItemCount += 1
            iIndex += 1
    return iIndex

def tokenize_semicolon(iObject, lObjects, token):
    iIndex = iObject
    iItemCount = 0
    while iItemCount < 3:
        if is_item(lObjects, iIndex):
            if object_value_is(lObjects, iIndex, ';'):
                assign_token(lObjects, iIndex, token) 
                return iIndex
            iItemCount += 1
        iIndex += 1
    return iObject

def print_debug(sTitle, iStart, iEnd, lObjects):
    print('--> ' + sTitle)
    sOutput = ''
    for iIndex in range(iStart, iEnd + 1):
        print(f'{iIndex} | {lObjects[iIndex]}')
        sOutput += (lObjects[iIndex].get_value())
    print(sOutput)

def print_line(lObjects, iStart):
    iIndex = iStart
    sOutput = ''
    while type(lObjects[iIndex]) != parser.carriage_return:
        sOutput += lObjects[iIndex].get_value()
        iIndex += 1
    print(sOutput)
