
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

def assign_next_token(token, iToken, lObjects):
    iCurrent = find_next_token(iToken, lObjects)
    try:
        lObjects[iCurrent] = token(lObjects[iCurrent].get_value())
        iCurrent+= 1
        return iCurrent
    except TypeError:
        lObjects[iToken] = token()
    return iToken

def assign_token(lObjects, iToken, token):
    iCurrent = find_next_token(iToken, lObjects)
    try:
        lObjects[iCurrent] = token(lObjects[iCurrent].get_value())
        iCurrent+= 1
        return iCurrent
    except TypeError:
        lObjects[iToken] = token()
    return iToken

def assign_next_token_if(sToken, token, iToken, lObjects):
    iCurrent = find_next_token(iToken, lObjects)
    if object_value_is(lObjects, iCurrent, sToken):
        lObjects[iCurrent] = token(lObjects[iCurrent].get_value())
        iCurrent += 1
        return iCurrent
    return iToken


def assign_next_token_if_not(sToken, token, iToken, lObjects):
    iCurrent = find_next_token(iToken, lObjects)
    if not object_value_is(lObjects, iCurrent, sToken):
        lObjects[iCurrent] = token(lObjects[iCurrent].get_value())
        iCurrent += 1
        return iCurrent
    return iToken


def assign_next_token_required(sToken, token, iToken, lObjects):
    iCurrent = find_next_token(iToken, lObjects)
    if object_value_is(lObjects, iCurrent, sToken):
        lObjects[iCurrent] = token(lObjects[iCurrent].get_value())
        return iCurrent + 1
    return iToken


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
        iIndex += 1
    else:
        iEnd = iIndex
        iStart = iStart
    return iStart, iEnd


def classify_next_token_if(sToken, token, iToken, lObjects):
    iCurrent = find_next_token(iToken, lObjects)
    if object_value_is(lObjects, iCurrent, sToken):
        iCurrent = assign_token(lObjects, iCurrent, token)
        return iCurrent
    return iToken

def classify_next_token(token, iToken, lObjects):
    iCurrent = find_next_token(iToken, lObjects)
    iCurrent = assign_token(lObjects, iCurrent, token)
    return iCurrent


def classify_token(sToken, token, iToken, lObjects):
    iToken = find_next_token(iToken, lObjects)
    if object_value_is(lObjects, iToken, sToken):
        iToken = assign_token(lObjects, iToken, token)
        return True
    return False


def find_in_range(sValue, iToken, sEnd, lObjects):
    iStart, iEnd = get_range(lObjects, iToken, sEnd)
    for iIndex in range(iStart, iEnd + 1):
        if object_value_is(lObjects, iIndex, sValue):
            return True
    return False


def find_in_next_n_tokens(sValue, iMax, iToken, lObjects):
    iTokenCount = 0
    iCurrent = iToken
    while iTokenCount < iMax:
        iCurrent = find_next_token(iCurrent, lObjects)
        iTokenCount += 1
        if object_value_is(lObjects, iCurrent, sValue):
            return True
        iCurrent += 1
    else:
        return False


def find_earliest_occurance(lEnd, iToken, lObjects):
    iEarliest = 9999999999999999999999999999
    for sEnd in lEnd:
        for iIndex in range(iToken, len(lObjects) - 1):
            if lObjects[iIndex].get_value() == sEnd:
                if iIndex < iEarliest:
                    sEarliest = lObjects[iIndex].get_value()
                    iEarliest = iIndex
    return sEarliest


def find_in_range_with_multiple_ends(sValue, iToken, lEnd, lObjects):
    iStart, iEnd = get_range(lObjects, iToken, sEarliest)
    for iIndex in range(iStart, iEnd + 1):
        if object_value_is(lObjects, iIndex, sValue):
            return True
    return False


def find_next_token(iToken, lObjects):
    while not is_item(lObjects, iToken):
        iToken += 1
    return iToken


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

def classify_semicolon(iToken, token, lObjects):
    find_next_token(iToken, lObjects)
    if classify_token(';', token, iToken, lObjects):
        iToken += 1
        return True
    return False


#def has_label(iObject, lObjects):
#    iItemCount = 0
#    iIndex = iObject
#    try:
#        while iItemCount < 2:
#            print(lObjects[iIndex].get_value())
#            if type(lObjects[iIndex]) == parser.item:
#                iItemCount += 1
#            iIndex += 1
#        else:
#            if lObjects[iIndex-1].get_value().lower() == ':':
#                return True
#    except IndexError:
#        return False
#    return False
    
def has_label(iObject, lObjects):
    iCurrent = find_next_token(iObject, lObjects)
    iCurrent = increment_token_count(iCurrent)
    iCurrent = find_next_token(iCurrent, lObjects)
    if object_value_is(lObjects, iCurrent, ':'):
        return True
    return False

#def tokenize_postponed(iObject, lObjects, token):
#    iIndex = iObject
#    iItemCount = 0
#    while iItemCount < 3:
#        if is_item(lObjects, iIndex):
#            if object_value_is(lObjects, iIndex, 'postponed'):
#                assign_token(lObjects, iIndex, token) 
#                return iIndex
#            iItemCount += 1
#        iIndex += 1
#    return iObject

def tokenize_postponed(iObject, lObjects, token):
    iIndex = find_next_token(iObject, lObjects)
    if object_value_is(lObjects, iIndex, 'postponed'):
        assign_token(lObjects, iIndex, token) 
        return iIndex + 1
    return iObject

def tokenize_label(iToken, lObjects, label_token, colon_token):
    iCurrent = find_next_token(iToken, lObjects)
    iItemCount = 0
    if has_label(iCurrent, lObjects):
        while iItemCount < 2:
            if is_item(lObjects, iCurrent):
                if iItemCount == 0:
                    assign_token(lObjects, iCurrent, label_token) 
                if iItemCount == 1:
                    assign_token(lObjects, iCurrent, colon_token) 
                iItemCount += 1
            iCurrent += 1
        return iCurrent
    return iToken

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

def print_token(iObject, lObjects):
    print(f'{iObject} | {lObjects[iObject].get_value()}')

def print_line(lObjects, iStart):
    iIndex = iStart
    sOutput = ''
    while type(lObjects[iIndex]) != parser.carriage_return:
        sOutput += lObjects[iIndex].get_value()
        iIndex += 1
    print(sOutput)

def token_is_semicolon(iObject, lObjects):
    if object_value_is(lObjects, iObject, ';'):
        return True
    return False

def token_is_comma(iObject, lObjects):
    if object_value_is(lObjects, iObject, ','):
        return True
    return False

def token_is_open_parenthesis(iObject, lObjects):
    if object_value_is(lObjects, iObject, '('):
        return True
    return False

def token_is_close_parenthesis(iObject, lObjects):
    if object_value_is(lObjects, iObject, ')'):
        return True
    return False

def increment_token_count(iToken):
    return iToken + 1


def is_next_token(sToken, iToken, lObjects):
    iCurrent = find_next_token(iToken, lObjects)
    if object_value_is(lObjects, iCurrent, sToken):
        return True
    return False


def classify_subelement_until(sToken, element, iToken, lObjects):
    iCurrent = iToken
    while not is_next_token(sToken, iCurrent, lObjects):
        iCurrent = element.classify(iCurrent, lObjects)
    return iCurrent

#def index_of_token(iObject, lObjects, sToken):
#    iReturn = iObject
#    while not utils.object_value_is(lObjects, iReturn, sToken):
#        iReturn += 1
#    else:
#        return iReturn
#    return -1

