
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


def have_guard_condition(iToken, lObjects):
    return is_next_token('(', iToken, lObjects)


def have_is_keyword(iToken, lObjects):
    return is_next_token('is', iToken, lObjects)


def assign_tokens_until(sToken, token, iToken, lObjects):
    iCurrent = iToken
    while not is_next_token(sToken, iCurrent, lObjects):
        iCurrent = assign_next_token(token, iCurrent, lObjects)
    return iCurrent


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


def assign_next_token_if_not_one_of(lTokens, token, iToken, lObjects):
    iCurrent = find_next_token(iToken, lObjects)
    if lObjects[iCurrent].get_value().lower() not in lTokens:
        lObjects[iCurrent] = token(lObjects[iCurrent].get_value())
        iCurrent += 1
        return iCurrent
    return iToken


def assign_next_token_required(sToken, token, iToken, lObjects):
    iCurrent = find_next_token(iToken, lObjects)
    if object_value_is(lObjects, iCurrent, sToken):
        lObjects[iCurrent] = token(lObjects[iCurrent].get_value())
        return iCurrent + 1
    else:
        print_error_message(sToken, token, iCurrent, lObjects)
    return iToken


def object_value_is(lAllObjects, iToken, sString):
    if lAllObjects[iToken].get_value().lower() == sString.lower():
        return True
    return False


def is_item(lAllObjects, iToken):
    if type(lAllObjects[iToken]) == parser.item:
        return True
    return False


def get_range(lObjects, iStart, sEnd):
    iIndex = iStart
    while lObjects[iIndex].get_value().lower() != sEnd:
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


def find_in_index_range(sValue, iStart, iEnd, lObjects):
    for iIndex in range(iStart, iEnd + 1):
        if object_value_is(lObjects, iIndex, sValue):
            return True
    return False


def are_next_consecutive_tokens(lTokens, iToken, lObjects):
    iMaxTokenCount = len(lTokens)
    iTokenCount = 0
    iCurrent = iToken
    while iTokenCount < iMaxTokenCount:
        iCurrent = find_next_token(iCurrent, lObjects)
        if not lTokens[iTokenCount] is None:
            if not is_next_token(lTokens[iTokenCount], iCurrent, lObjects):
                return False
        iCurrent += 1
        iTokenCount += 1
    else:
        return True


def are_next_consecutive_token_types(lTypes, iToken, lObjects):
    iMaxTokenCount = len(lTypes)
    iTokenCount = 0
    iCurrent = iToken
    try:
        while iTokenCount < iMaxTokenCount:
            iCurrent = find_next_token(iCurrent, lObjects)
            if not lTypes[iTokenCount] is None:
                if not isinstance(lObjects[iCurrent], lTypes[iTokenCount]):
                    return False
            iCurrent += 1
            iTokenCount += 1
        else:
            return True
    except IndexError:
        return False


def find_in_next_n_tokens(sValue, iMax, iToken, lObjects):
    iEnd = len(lObjects)
    iTokenCount = 0
    iCurrent = iToken
    while iTokenCount < iMax:
        iCurrent = find_next_token(iCurrent, lObjects)
        iTokenCount += 1
        if object_value_is(lObjects, iCurrent, sValue):
            return True
        iCurrent += 1
        if iCurrent == iEnd:
            return False
    else:
        return False


def find_earliest_occurance_ignoring_matched_parenthesis(lEnd, iToken, lObjects):
    print('--> find_earliest_occurance_ignoring_matched_parenthesis')
    iEarliest = 9999999999999999999999999999
    print(lEnd)
    for sEnd in lEnd:
        print(f'----> Searching for {sEnd}')
        iOpenParenthesis = 0
        iCloseParenthesis = 0
        for iIndex in range(iToken, len(lObjects) - 1):
            if token_is_open_parenthesis(iIndex, lObjects):
                iOpenParenthesis +=1
            print(f'{iIndex} | {lObjects[iIndex].get_value()} | {iOpenParenthesis} | {iCloseParenthesis}')
            if lObjects[iIndex].get_value().lower() == sEnd:
                if iOpenParenthesis == iCloseParenthesis:
                    if iIndex < iEarliest:
                        sEarliest = lObjects[iIndex].get_value()
                        iEarliest = iIndex
                    break
            if iIndex == iEarliest:
                break
            if token_is_close_parenthesis(iIndex, lObjects):
                iCloseParenthesis += 1
    print(f'<-- find_earliest_occurance_ignoring_matched_parenthesis :: {sEarliest}')
    return sEarliest


def find_earliest_occurance(lEnd, iToken, lObjects):
    iEarliest = 9999999999999999999999999999
    for sEnd in lEnd:
        for iIndex in range(iToken, len(lObjects) - 1):
            if lObjects[iIndex].get_value().lower() == sEnd:
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
    iCurrent = iToken
    iEnd = len(lObjects)
    while not is_item(lObjects, iCurrent):
        iCurrent += 1
        if iCurrent == iEnd:
            return iToken
    return iCurrent


def detect_submodule(iToken, lObjects, module):
    iEnd = len(lObjects) - 1  
    iLast = -1
    iReturn = iToken
    while iLast != iReturn:
        if iReturn == iEnd:
            return iReturn
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


def has_label(iObject, lObjects):
    iCurrent = find_next_token(iObject, lObjects)
    iCurrent = increment_token_count(iCurrent)
    iCurrent = find_next_token(iCurrent, lObjects)
    if object_value_is(lObjects, iCurrent, ':'):
        return True
    return False


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


def print_next_token(iObject, lObjects):
    iCurrent = find_next_token(iObject, lObjects)
    iLine = calculate_line_number(iObject, lObjects)
    print(f'{iLine} | {iCurrent} | {lObjects[iCurrent].get_value()}')


def print_token(iObject, lObjects):
    iLine = calculate_line_number(iObject, lObjects)
    print(f'{iLine} | {iObject} | {lObjects[iObject].get_value()} | {lObjects[iObject]}')


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


def is_next_token_one_of(lTokens, iToken, lObjects):
    iCurrent = find_next_token(iToken, lObjects)
    if lObjects[iCurrent].get_value().lower() in lTokens:
        return True
    return False


def detect_subelement_until(sToken, element, iToken, lObjects):
    iCurrent = iToken
    while not is_next_token(sToken, iCurrent, lObjects):
        iLast = iCurrent
        iCurrent = element.detect(iCurrent, lObjects)
        if iLast == iCurrent:
            return iCurrent
    return iCurrent


def classify_subelement_until(sToken, element, iToken, lObjects):
    iCurrent = iToken
    while not is_next_token(sToken, iCurrent, lObjects):
        iCurrent = element.classify(iCurrent, lObjects)
    return iCurrent


def calculate_line_number(iToken, lObjects):
    iReturn = 1
    for iIndex in range(0, iToken):
        if type(lObjects[iIndex]) == parser.carriage_return:
            iReturn += 1
    return iReturn


def calculate_column(iToken, lObjects):
    iColumn = 0
    for iCarriageReturn in range(iToken, 0, -1):
        if type(lObjects[iCarriageReturn]) == parser.carriage_return:
            break;
    for iIndex in range(iCarriageReturn + 1, iToken):
        iColumn += len(lObjects[iIndex].get_value())
    iColumn += 1
    return iColumn


def print_error_message(sToken, token, iToken, lObjects):
    sFoundToken = lObjects[iToken].get_value()
    iLine = calculate_line_number(iToken, lObjects)
    iColumn = calculate_column(iToken, lObjects)
    sModuleName = extract_module_name(token)
    print(f'Error: Unknown token in {sModuleName}({iLine}:{iColumn})')
    print(f'       Expecting {sToken}, found {sFoundToken}')
    exit()


def extract_module_name(token):
    return token.__module__.split('.')[-1]


def keyword_found(sKeyword, iToken, lObjects):
    if find_in_next_n_tokens(':', 2, iToken, lObjects):
        if find_in_next_n_tokens(sKeyword, 3, iToken, lObjects):
            return True
        else:
            return False
    if is_next_token(sKeyword, iToken, lObjects):
        return True
    return False


def is_next_token_in_list(lUntils, iToken, lObjects):
    iCurrent = find_next_token(iToken, lObjects)
    if lObjects[iCurrent].get_value().lower() in lUntils:
        return True
    return False


def combine_two_token_class_lists(lToi_a, lToi_b):
    '''
    Takes two lists that contain Token classes and merges them into a single list.
    The final list is ordered by the iStartIndex attribute on the Token classes.
    '''
    if len(lToi_a) == 0:
        return lToi_b
    if len(lToi_b) == 0:
        return lToi_a
    lReturn = lToi_a.copy()
    for oToi in lToi_b:
        bInserted = False
        for iIndex, oReturn in enumerate(lReturn):
            if oToi.iStartIndex < oReturn.iStartIndex:
                lReturn.insert(iIndex, oToi)
                bInserted = True
                break
        if not bInserted:
            lReturn.append(oToi)
    return lReturn


def does_length_of_tokens_exceed(lObjects, iLength):

    iTotalLength = 0
    for oObject in lObjects:
        iTotalLength += len(oObject.get_value())
    if iTotalLength > iLength:
        return True
    return False


def remove_carriage_returns_from_token_list(lTokens):
    lMyTokens = []
    for oToken in lTokens:
        if isinstance(oToken, parser.carriage_return):
            continue
        lMyTokens.append(oToken)
    return lMyTokens 


def remove_consecutive_whitespace_tokens(lTokens):
    lMyTokens = []
    for iToken, oToken in enumerate(lTokens):
        if iToken == 0:
            lMyTokens.append(oToken)
        else:
            if isinstance(oToken, parser.whitespace) and isinstance(lTokens[iToken - 1], parser.whitespace):
                continue
            else:
                lMyTokens.append(oToken)
    return lMyTokens


def remove_whitespace_from_token_list(lTokens):
    lMyTokens = []
    for oToken in lTokens:
        if isinstance(oToken, parser.whitespace):
            continue
        lMyTokens.append(oToken)
    return lMyTokens 


def remove_comment_at_end_of_token_list(lTokens):
    if isinstance(lTokens[-1], parser.comment):
        return lTokens[:-1]
    return lTokens
