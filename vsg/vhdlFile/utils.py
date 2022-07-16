
from vsg import exceptions
from vsg import parser

from vsg.token import direction
from vsg.token import choice
from vsg.token import element_association
from vsg.token import exponent
from vsg.token import predefined_attribute

from vsg.token.ieee.std_logic_1164 import types


def assign_tokens_until(sToken, token, iToken, lObjects):
    iCurrent = iToken
    while not is_next_token(sToken, iCurrent, lObjects):
        iCurrent = assign_next_token(token, iCurrent, lObjects)
    return iCurrent


def assign_next_token(token, iToken, lObjects):
    iCurrent = find_next_token(iToken, lObjects)
    try:
        lObjects[iCurrent] = token(lObjects[iCurrent].get_value())
    except TypeError:
        lObjects[iCurrent] = token()
    iCurrent+= 1
    return iCurrent


def assign_token(lObjects, iToken, token):
    iCurrent = find_next_token(iToken, lObjects)
    try:
        lObjects[iCurrent] = token(lObjects[iCurrent].get_value())
    except TypeError:
        lObjects[iToken] = token()
    return iToken + 1


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


def assign_tokens_until_matching_closing_paren(token, iToken, lObjects):
    iCounter = 1
    iCurrent = iToken
    while iCurrent < len(lObjects):
        iCurrent = find_next_token(iCurrent, lObjects)
        iCounter = update_paren_counter(iCurrent, lObjects, iCounter)
        if token_is_close_parenthesis(iCurrent, lObjects) and iCounter == 0:
            return iCurrent
        lObjects[iCurrent] = token(lObjects[iCurrent].get_value())


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
    iEnd = iIndex
    iStart = iStart
    return iStart, iEnd


def classify_next_token(token, iToken, lObjects):
    iCurrent = find_next_token(iToken, lObjects)
    iCurrent = assign_token(lObjects, iCurrent, token)
    return iCurrent


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

    return True


def are_next_consecutive_token_types(lTypes, iToken, lObjects):
    iMaxTokenCount = len(lTypes)
    iTokenCount = 0
    iCurrent = iToken
    try:
        while iTokenCount < iMaxTokenCount:
            if not lTypes[iTokenCount] is None:
                if not isinstance(lObjects[iCurrent], lTypes[iTokenCount]):
                    return False
            iCurrent += 1
            iTokenCount += 1
        return True
    except IndexError:
        return False


def are_next_consecutive_token_types_ignoring_whitespace(lTypes, iToken, lObjects):
    iMaxTokenCount = len(lTypes)
    iTokenCount = 0
    iCurrent = iToken
    try:
        while iTokenCount < iMaxTokenCount:
            iCurrent = find_next_non_whitespace_token(iCurrent, lObjects)
            if not lTypes[iTokenCount] is None:
                if not isinstance(lObjects[iCurrent], lTypes[iTokenCount]):
                    return False
            iCurrent += 1
            iTokenCount += 1
        return True
    except IndexError:
        return False

def are_previous_consecutive_token_types_ignoring_whitespace(lTypes, iToken, lObjects):
    iMinTokenCount = 0
    iTokenCount = len(lTypes)
    iCurrent = iToken
    try:
        while iTokenCount != iMinTokenCount:
            iCurrent = find_previous_non_whitespace_token(iCurrent, lObjects)
            if not lTypes[iTokenCount - 1] is None:
                if not isinstance(lObjects[iCurrent], lTypes[iTokenCount - 1]):
                    return False
            iCurrent -= 1
            iTokenCount -= 1
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
    return False


def find_earliest_occurance(lEnd, iToken, lObjects):
    iEarliest = 9999999999999999999999999999
    for sEnd in lEnd:
        for iIndex in range(iToken, len(lObjects) - 1):
            if lObjects[iIndex].get_value().lower() == sEnd:
                if iIndex < iEarliest:
                    sEarliest = lObjects[iIndex].get_value()
                    iEarliest = iIndex
    return sEarliest


def find_next_token(iToken, lObjects):
    for iCurrent in range(iToken, len(lObjects)):
        if is_item(lObjects, iCurrent):
            return iCurrent
    return iToken


def find_next_non_whitespace_token(iToken, lObjects):
    iCurrent = iToken
    for iIndex in range(iToken, len(lObjects)):
        oToken = lObjects[iIndex]
        if token_is_whitespace_or_comment(oToken):
            continue
        return iIndex
    return iCurrent


def find_previous_non_whitespace_token(iToken, lObjects):
    iCurrent = iToken
    for iIndex in range(iToken, -1, -1):
        oToken = lObjects[iIndex]
        if token_is_whitespace_or_comment(oToken):
            continue
        return iIndex
    return iCurrent


def detect_submodule(iToken, lObjects, module):
    iLast = -1
    iReturn = iToken
    while iLast != iReturn:
        if is_next_token('end', iReturn, lObjects):
            return iToken
        iReturn = find_next_token(iReturn, lObjects)
        iLast = iReturn
        iReturn = module.detect(iReturn, lObjects)

    return iReturn


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
    while not isinstance(lObjects[iIndex], parser.carriage_return):
        sOutput += lObjects[iIndex].get_value()
        iIndex += 1
    print(sOutput)


def print_lines(lObjects):
    sOutput = ''
    for oObject in lObjects:
        sOutput += oObject.get_value()
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


def token_is_assignment_operator(iObject, lObjects):
    if object_value_is(lObjects, iObject, '<='):
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
        if isinstance(lObjects[iIndex], parser.carriage_return):
            iReturn += 1
    return iReturn


def calculate_column(iToken, lObjects):
    iColumn = 0
    for iCarriageReturn in range(iToken, 0, -1):
        if isinstance(lObjects[iCarriageReturn], parser.carriage_return):
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

    sErrorMessage = '\n'
    sErrorMessage += f'Error: Unexpected token detected while parsing {sModuleName} @ Line {iLine}, Column {iColumn} in file {lObjects[0].get_filename()}'
    sErrorMessage += '\n'
    sErrorMessage += f'       Expecting : {sToken}'
    sErrorMessage += '\n'
    sErrorMessage += f'       Found     : {sFoundToken}'
    sErrorMessage += '\n'

    raise exceptions.ClassifyError(sErrorMessage)


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


def remove_comments_from_token_list(lTokens):
    lMyTokens = []
    for oToken in lTokens:
        if isinstance(oToken, parser.comment):
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


def does_token_type_match(oToken, oType):
    if isinstance(oToken, oType):
        return True
    return False


def remove_trailing_whitespace(lTokens):
    lTokens.reverse()
    for iIndex in range(0, len(lTokens)):
        if token_is_whitespace(lTokens[iIndex]):
            continue
        else:
            lMyTokens = lTokens[iIndex:]
            lMyTokens.reverse()
            return lMyTokens
    else:
        return lTokens


def remove_trailing_whitespace_and_comments(lTokens):
    lTokens.reverse()
    for iIndex in range(0, len(lTokens)):
        if token_is_whitespace_or_comment(lTokens[iIndex]):
            continue
        else:
            lMyTokens = lTokens[iIndex:]
            lMyTokens.reverse()
            return lMyTokens
    else:
        return lTokens


def remove_leading_whitespace_and_comments(iToken, lTokens):
    for iIndex in range(0, len(lTokens)):
        if token_is_whitespace_or_comment(lTokens[iIndex]):
            continue
        else:
            return iToken + iIndex + 1, lTokens[iIndex:]
    else:
        return iToken, lTokens


def token_is_whitespace_or_comment(oToken):
    if isinstance(oToken, parser.whitespace) or \
       isinstance(oToken, parser.carriage_return) or \
       isinstance(oToken, parser.comment) or \
       isinstance(oToken, parser.blank_line) or \
       isinstance(oToken, parser.preprocessor):
        return True
    else:
        return False


def token_is_whitespace(oToken):
    if isinstance(oToken, parser.whitespace) or \
       isinstance(oToken, parser.carriage_return) or \
       isinstance(oToken, parser.blank_line) or \
       isinstance(oToken, parser.preprocessor):
        return True
    else:
        return False


def increment_line_number(iLine, oToken):
    if isinstance(oToken, parser.carriage_return):
        return iLine + 1
    return iLine


def decrement_line_number(iLine, oToken):
    if isinstance(oToken, parser.carriage_return):
        return iLine - 1
    return iLine


def count_carriage_returns(lTokens):
    iReturn = 0
    for oToken in lTokens:
        iReturn = increment_line_number(iReturn, oToken)
    return iReturn


def increment_comment_counter(iComment, oToken):
    if isinstance(oToken, parser.comment):
        return iComment + 1
    return iComment


def find_carriage_return(lTokens, iToken=0):
    for iIndex in range(iToken, len(lTokens)):
        if isinstance(lTokens[iIndex], parser.carriage_return):
            return iIndex
    return None


def count_token_types_in_list_of_tokens(oType, lTokens):
    iReturn = 0
    for oToken in lTokens:
        if isinstance(oToken, oType):
            iReturn += 1
    return iReturn


def does_token_type_exist_in_list_of_tokens(oType, lTokens):
    if count_token_types_in_list_of_tokens(oType, lTokens) == 0:
        return False
    return True


def get_toi_parameters(oToi):
    return oToi.get_line_number(), oToi.get_tokens()


def does_token_start_line(iToken, lTokens):
    if isinstance(lTokens[iToken - 1], parser.whitespace) and isinstance(lTokens[iToken - 2], parser.carriage_return):
        return True
    if isinstance(lTokens[iToken - 1], parser.carriage_return):
        return True
    return False


def convert_token_list_to_string(lTokens):
    sReturn = ''
    for oToken in lTokens:
        sReturn += oToken.get_value()
    return sReturn


def fix_blank_lines(lTokens):
    lReturn = []
    for iToken, oToken in enumerate(lTokens):
        try:
            if isinstance(oToken, parser.carriage_return) and isinstance(lTokens[iToken + 1], parser.carriage_return):
                lReturn.append(oToken)
                lReturn.append(parser.blank_line())
                continue
        except IndexError:
            pass
        try:
            if isinstance(lTokens[iToken - 1], parser.carriage_return) and isinstance(oToken, parser.whitespace) and isinstance(lTokens[iToken + 1], parser.carriage_return):
                lReturn.append(parser.blank_line())
                continue
        except IndexError:
            pass
        lReturn.append(oToken)

    return lReturn


def fix_trailing_whitespace(lTokens):
    lReturn = []
    for iToken, oToken in enumerate(lTokens):
        try:
            if isinstance(oToken, parser.carriage_return) and isinstance(lTokens[iToken - 1], parser.whitespace):
                lReturn.pop()
                lReturn.append(oToken)
                continue
        except IndexError:
            pass
        lReturn.append(oToken)

    return lReturn


def is_whitespace(oObject):
    if isinstance(oObject, parser.carriage_return):
        return True
    if isinstance(oObject, parser.blank_line):
        return True
    if isinstance(oObject, parser.comment):
        return True
    if isinstance(oObject, parser.whitespace):
        return True
    if isinstance(oObject, parser.preprocessor):
        return True
    return False


def read_vhdlfile(sFileName):
    try:
        lLines = []
        with open(sFileName, encoding='utf-8') as oFile:
            for sLine in oFile:
                lLines.append(sLine)
        return lLines, None
    except UnicodeDecodeError:
        lLines = []
        with open(sFileName, encoding="ISO-8859-1") as oFile:
            for sLine in oFile:
                lLines.append(sLine)
        return lLines, None
    except OSError as e:
        return [], e


def is_token_at_end_of_line(iToken, lTokens):
    iMyToken = iToken + 1
    if are_next_consecutive_token_types([parser.carriage_return], iMyToken, lTokens):
        return True
    if are_next_consecutive_token_types([parser.whitespace, parser.carriage_return], iMyToken, lTokens):
        return True
    if are_next_consecutive_token_types([parser.comment, parser.carriage_return], iMyToken, lTokens):
        return True
    if are_next_consecutive_token_types([parser.whitespace, parser.comment, parser.carriage_return], iMyToken, lTokens):
        return True
    return False


def find_next_token_with_value(iToken, sValue, lTokens):
    for iIndex, oToken in enumerate(lTokens[iToken::]):
        if oToken.get_value() == sValue:
            return iToken + iIndex
    return None


def all_assignments_inside_parenthesis(iToken, sStop, lTokens):
    iStop = find_next_token_with_value(iToken, sStop, lTokens)
    iParen = 0
    for iIndex in range(iToken, iStop + 1):
        iParen = update_paren_counter(iIndex, lTokens, iParen)
        if token_is_assignment_operator(iIndex, lTokens) and iParen == 0:
            return False
    return True


def update_paren_counter(iToken, lTokens, iCounter):
    if token_is_open_parenthesis(iToken, lTokens):
        return iCounter + 1
    if token_is_close_parenthesis(iToken, lTokens):
        return iCounter - 1
    return iCounter


def assignment_operator_found(iToken, lObjects):
    if find_in_range('<=', iToken, ';', lObjects):
        if all_assignments_inside_parenthesis(iToken, ';', lObjects):
            return False
        return True
    return False


def assign_special_tokens(lObjects, iCurrent, oType):
    sValue = lObjects[iCurrent].get_value()
    if sValue == ')':
        assign_token(lObjects, iCurrent, parser.close_parenthesis)
    elif sValue == '(':
        assign_token(lObjects, iCurrent, parser.open_parenthesis)
    elif sValue == '-':
        if isinstance(lObjects[iCurrent - 1], exponent.e_keyword):
            assign_token(lObjects, iCurrent, exponent.minus_sign)
        else:
            assign_token(lObjects, iCurrent, parser.todo)
    elif sValue == '+':
        if isinstance(lObjects[iCurrent - 1], exponent.e_keyword):
            assign_token(lObjects, iCurrent, exponent.plus_sign)
        else:
            assign_token(lObjects, iCurrent, parser.todo)
    elif sValue == '*':
        assign_token(lObjects, iCurrent, parser.todo)
    elif sValue == '**':
        assign_token(lObjects, iCurrent, parser.todo)
    elif sValue == '/':
        assign_token(lObjects, iCurrent, parser.todo)
    elif sValue.lower() == 'downto':
        assign_token(lObjects, iCurrent, direction.downto)
    elif sValue.lower() == 'to':
        assign_token(lObjects, iCurrent, direction.to)
    elif sValue.lower() == 'std_logic_vector':
        assign_token(lObjects, iCurrent, types.std_logic_vector)
    elif sValue.lower() == 'std_ulogic_vector':
        assign_token(lObjects, iCurrent, types.std_ulogic_vector)
    elif sValue.lower() == 'std_ulogic':
        assign_token(lObjects, iCurrent, types.std_ulogic)
    elif sValue.lower() == 'std_logic':
        assign_token(lObjects, iCurrent, types.std_logic)
    elif sValue.lower() == 'integer':
        assign_token(lObjects, iCurrent, types.integer)
    elif sValue.lower() == 'signed':
        assign_token(lObjects, iCurrent, types.signed)
    elif sValue.lower() == 'unsigned':
        assign_token(lObjects, iCurrent, types.unsigned)
    elif sValue.lower() == 'natural':
        assign_token(lObjects, iCurrent, types.natural)
    elif sValue.lower() == 'others':
        assign_token(lObjects, iCurrent, choice.others_keyword)
    elif sValue.lower() == '=>':
        assign_token(lObjects, iCurrent, element_association.assignment)
    elif sValue.lower() == 'e':
        if lObjects[iCurrent + 1].get_value().isdigit() or lObjects[iCurrent + 1].get_value() == '-' or lObjects[iCurrent + 1].get_value() == '+':
            assign_token(lObjects, iCurrent, exponent.e_keyword)
        else:
            assign_token(lObjects, iCurrent, oType)
    elif exponent_detected(lObjects, iCurrent):
        assign_token(lObjects, iCurrent, exponent.integer)
    else:
        assign_token(lObjects, iCurrent, oType)


def exponent_detected(lObjects, iCurrent):
    if isinstance(lObjects[iCurrent - 1], exponent.e_keyword):
        return True
    if isinstance(lObjects[iCurrent - 1], exponent.plus_sign):
        return True
    if isinstance(lObjects[iCurrent - 1], exponent.minus_sign):
        return True
    return False


def classify_predefined_types(lObjects, iCurrent):
    if not isinstance(lObjects[iCurrent], parser.todo):
        return
    if lObjects[iCurrent].get_value().lower() in predefined_attribute.values:
        if lObjects[iCurrent].get_value().lower() == 'event':
            assign_token(lObjects, iCurrent, predefined_attribute.event_keyword)
        else:
            assign_token(lObjects, iCurrent, predefined_attribute.keyword)
