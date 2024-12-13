# -*- coding: utf-8 -*-

from vsg import parser, token
from vsg.vhdlFile import utils


def remove_optional_item(oViolation, oInsertToken=None):
    lTokens = oViolation.get_tokens()
    if isinstance(lTokens[0], parser.whitespace):
        oViolation.set_tokens([])
    else:
        oViolation.set_tokens([lTokens[0]])


def is_single_line(oToi):
    lTokens = oToi.get_tokens()
    for oToken in lTokens:
        if isinstance(oToken, parser.carriage_return):
            return False
    return True


def number_of_carriage_returns(lTokens):
    iReturn = 0
    for oToken in lTokens:
        if isinstance(oToken, parser.carriage_return):
            iReturn += 1
    return iReturn


def number_of_tokens_from_token_list_in_token_list(lTokens, lTokenList):
    iReturn = 0
    for oToken in lTokens:
        iReturn += number_of_tokens_in_token_list(oToken, lTokenList)
    return iReturn


def number_of_tokens_in_token_list(oToken, lTokens):
    iReturn = 0
    for oTokenItem in lTokens:
        if oToken == type(oTokenItem):
            iReturn += 1
    return iReturn


def does_line_start_with_comment(lTokens):
    if isinstance(lTokens[0], parser.comment):
        return True
    if isinstance(lTokens[0], parser.whitespace) and isinstance(lTokens[1], parser.comment):
        return True
    return False


def get_toi_parameters(oToi):
    return oToi.get_line_number(), oToi.get_tokens()


def insert_token(lTokens, index, oToken):
    try:
        oToken = update_code_tags(lTokens[index], oToken)
    except TypeError:
        oToken = update_code_tags(lTokens[0], oToken)
    except IndexError:
        oToken = update_code_tags(lTokens[0], oToken)

    if index == "end":
        lTokens.insert(len(lTokens), oToken)
    else:
        lTokens.insert(index, oToken)


def append_token(lTokens, oToken):
    oToken = update_code_tags(lTokens[-1], oToken)
    lTokens.append(oToken)


def update_code_tags(oToken1, oToken2):
    oToken2.code_tags = oToken1.code_tags
    return oToken2


def insert_whitespace(lTokens, index, num=1, sString=" "):
    if sString == " ":
        insert_token(lTokens, index, parser.whitespace(" " * num))
    else:
        oToken = parser.whitespace("\t" * num)
        oToken.has_tabs = True
        insert_token(lTokens, index, oToken)


def insert_new_whitespace(lTokens, index, sWhitespace):
    oToken = parser.whitespace(sWhitespace)
    if "\t" in sWhitespace:
        oToken.has_tabs = True
    insert_token(lTokens, index, oToken)


def insert_carriage_return(lTokens, index):
    insert_token(lTokens, index, parser.carriage_return())


def insert_blank_line(lTokens, index):
    insert_token(lTokens, index, parser.blank_line())


def append_whitespace(lTokens, num=1):
    append_token(lTokens, parser.whitespace(" " * num))


def append_carriage_return(lTokens):
    append_token(lTokens, parser.carriage_return())


def get_index_of_token_in_list(oToken, lTokens):
    for iToken, token in enumerate(lTokens):
        if isinstance(token, oToken):
            return iToken
    return None


def get_last_index_of_token_in_list(oToken, lTokens):
    iReturn = None
    for iToken, token in enumerate(lTokens):
        if isinstance(token, oToken):
            iReturn = iToken
    return iReturn


def get_index_of_token_in_list_after_index(oToken, lTokens, iIndex):
    for iToken, token in enumerate(lTokens):
        if iToken > iIndex and isinstance(token, oToken):
            return iToken
    return None


def get_indexes_of_token_in_list(oToken, lTokens):
    lReturn = []
    for iToken, token in enumerate(lTokens):
        if isinstance(token, oToken):
            lReturn.append(iToken)
    return lReturn


def get_number_of_carriage_returns_before_token(oStopToken, lTokens):
    iReturn = 0
    for oToken in lTokens:
        if isinstance(oToken, parser.carriage_return):
            iReturn += 1
        if isinstance(oToken, oStopToken):
            break
    return iReturn


def get_number_of_carriage_returns_before_last_token(oStopToken, lTokens):
    iReturn = 0
    iCarriage = 0
    for oToken in lTokens:
        if isinstance(oToken, parser.carriage_return):
            iCarriage += 1
        if isinstance(oToken, oStopToken):
            iReturn = iCarriage
    return iReturn


def whitespace_before_token_index(lTokens, iIndex):
    if isinstance(lTokens[iIndex - 1], parser.whitespace):
        return True
    return False


def remove_token_sequence_from_token_list(lRemoveTokens, lTokens):
    lSliceIndexes = find_slice_indexes_of_token_sequence_in_token_list(lRemoveTokens, lTokens)
    return remove_slices_from_token_list(lTokens, lSliceIndexes)


def find_slice_indexes_of_token_sequence_in_token_list(lRemoveTokens, lTokens):
    iTokenListLength = len(lTokens)
    iLength = len(lRemoveTokens)
    lReturn = []
    for iIndex in range(0, iTokenListLength - 1 - iLength):
        if is_token_sequence_at_index_in_token_list(lRemoveTokens, iIndex, lTokens):
            lReturn.append([iIndex, iIndex + iLength])
    return lReturn


def is_token_sequence_at_index_in_token_list(lRemoveTokens, iIndex, lTokens):
    iLength = len(lRemoveTokens)
    for iToken in range(0, iLength):
        if not isinstance(lTokens[iIndex + iToken], lRemoveTokens[iToken]):
            return False
    return True


def remove_slices_from_token_list(lTokens, lSlices):
    lReturn = lTokens
    lSlices.reverse()
    for lSlice in lSlices:
        lReturn = remove_slice_from_token_list(lReturn, lSlice)
    return lReturn


def remove_slice_from_token_list(lTokens, lSlice):
    iStart = lSlice[0]
    iEnd = lSlice[1]
    return lTokens[0:iStart] + lTokens[iEnd::]


def token_is_carriage_return(oToken):
    if isinstance(oToken, parser.carriage_return):
        return True
    return False


def token_is_comment(oToken):
    if isinstance(oToken, parser.comment):
        return True
    return False


def token_is_blank_line(oToken):
    if isinstance(oToken, parser.blank_line):
        return True
    return False


def token_is_open_paren(oToken):
    if isinstance(oToken, parser.open_parenthesis):
        return True
    return False


def token_is_close_paren(oToken):
    if isinstance(oToken, parser.close_parenthesis):
        return True
    return False


def token_is_parenthesis(oToken):
    if token_is_open_paren(oToken) or token_is_close_paren(oToken):
        return True
    return False


def token_is_whitespace(oToken):
    if isinstance(oToken, parser.whitespace):
        return True
    return False


def token_list_begins_with_close_paren(lTokens):
    if isinstance(lTokens[0], parser.whitespace) and isinstance(lTokens[1], parser.close_parenthesis):
        return True
    if isinstance(lTokens[0], parser.close_parenthesis):
        return True
    return False


def token_list_starts_with_paren(lTokens, iIndex=0):
    iToken = utils.find_next_non_whitespace_token(iIndex, lTokens)
    if isinstance(lTokens[iToken], parser.open_parenthesis):
        return True
    return False


def token_at_the_beginning_of_a_line(oToken, lTokens):
    if isinstance(lTokens[0], parser.whitespace) and isinstance(lTokens[1], oToken):
        return True
    if isinstance(lTokens[0], oToken):
        return True
    return False


def token_at_beginning_of_line_in_token_list(iToken, lTokens):
    if isinstance(lTokens[iToken - 1], parser.carriage_return):
        return True
    if isinstance(lTokens[iToken - 1], parser.whitespace) and isinstance(lTokens[iToken - 2], parser.carriage_return):
        return True
    return False


def token_list_is_the_beginning_of_a_line(lTokens):
    if isinstance(lTokens[0], parser.carriage_return) and isinstance(lTokens[1], parser.whitespace):
        return True
    if isinstance(lTokens[1], parser.carriage_return):
        return True
    return False


def token_is_at_end_of_line(iToken, lTokens):
    if token_is_carriage_return(lTokens[iToken + 1]):
        return True
    if token_is_comment(lTokens[iToken + 1]):
        return True
    if token_is_whitespace(lTokens[iToken + 1]) and token_is_comment(lTokens[iToken + 2]):
        return True
    return False


def left_most_token_is_at_the_end_of_a_line(lTokens):
    return token_is_at_end_of_line(0, lTokens)


def whitespace_is_larger_than_a_single_character(lTokens):
    if lTokens[1].get_value() != " ":
        return True
    return False


def remove_toi_if_token_is_at_the_end_of_the_line(lToi):
    lReturn = []
    for oToi in lToi:
        lTokens = oToi.get_tokens()
        if left_most_token_is_at_the_end_of_a_line(lTokens):
            continue
        lReturn.append(oToi)
    return lReturn


def lowercase_list(lList):
    lReturn = []
    for sItem in lList:
        lReturn.append(sItem.lower())
    return lReturn


def extract_identifiers_with_mode_of_input(lToi):
    return extract_identifiers_with_mode(lToi, token.mode.in_keyword)


def extract_identifiers_with_mode_of_out(lToi):
    return extract_identifiers_with_mode(lToi, token.mode.out_keyword)


def extract_identifiers_with_mode_of_inout(lToi):
    return extract_identifiers_with_mode(lToi, token.mode.inout_keyword)


def extract_identifiers_with_mode_of_buffer(lToi):
    return extract_identifiers_with_mode(lToi, token.mode.buffer_keyword)


def extract_identifiers_with_mode_of_linkage(lToi):
    return extract_identifiers_with_mode(lToi, token.mode.linkage_keyword)


def extract_identifiers_with_mode(lToi, oTokenType):
    lReturn = []
    for oToi in lToi:
        if oToi.token_type_exists(oTokenType):
            iIndex = oToi.get_index_of_token_matching(parser.identifier)
            lReturn.append(oToi.extract_tokens(iIndex, iIndex))
    return lReturn


def remove_leading_whitespace_tokens(lTokens):
    if len(lTokens) > 1 and isinstance(lTokens[0], parser.whitespace):
        lTokens.pop(0)


def change_all_whitespace_to_single_character(lTokens):
    for oToken in lTokens:
        if isinstance(oToken, parser.whitespace):
            oToken.set_value(" ")


def token_is_at_beginning_of_line(lTokens):
    if isinstance(lTokens[0], parser.carriage_return):
        return True
    if isinstance(lTokens[1], parser.carriage_return):
        return True
    return False


def update_open_paren_counter(oToken, iOpenParen):
    if token_is_open_paren(oToken):
        return iOpenParen + 1
    return iOpenParen


def update_close_paren_counter(oToken, iCloseParen):
    if token_is_close_paren(oToken):
        return iCloseParen + 1
    return iCloseParen


def update_paren_counter(oToken, iParen):
    if token_is_open_paren(oToken):
        iParen += 1
    elif token_is_close_paren(oToken):
        iParen -= 1
    return iParen


def analyze_with_function(self, oToi, oTokenType, fFunction):
    iLine, lTokens = get_toi_parameters(oToi)

    for iToken, oToken in enumerate(lTokens):
        iLine = utils.increment_line_number(iLine, oToken)
        if isinstance(oToken, oTokenType):
            oToi.set_meta_data("iStartLine", iLine)
            oToi.set_meta_data("iStart", iToken)
            oToi.set_meta_data("iToken", iToken)
            fFunction(self, oToi)


def token_exists_in_token_type_list(oToken, lTypeTokens):
    for oTokenType in lTypeTokens:
        if isinstance(oToken, oTokenType):
            return True
    return False


def is_next_token_ignoring_whitespace(oToken, iToken, lTokens):
    iToken = utils.find_next_non_whitespace_token(iToken + 1, lTokens)
    if isinstance(lTokens[iToken], oToken):
        return True
    return False


def array_detected_after_assignment_operator(assignment_operator, oToi):
    lTokens = oToi.get_tokens()
    if not open_paren_after_assignment_operator(assignment_operator, lTokens):
        return False
    if open_paren_after_assignment_operator_is_aggregate(assignment_operator, lTokens):
        return True
    if open_paren_after_assignment_operator_id_matches_last_paren_id(assignment_operator, lTokens):
        return True
    if open_paren_after_assignment_operator_is_followed_by_aggregate_open_parenthesis(assignment_operator, lTokens):
        return True
    if not close_paren_detected_at_end_of_tokens(lTokens):
        return False

    iParen = 0
    bFirstTokenFound = False
    iParenId = -1
    for oToken in lTokens:
        if iParenId == -1 and token_is_open_paren(oToken):
            iParenId = oToken.iId
        if second_open_paren_detected_after_first_open_paren_was_closed(bFirstTokenFound, iParen, oToken):
            return False
        iParen = update_paren_counter(oToken, iParen)
        if not bFirstTokenFound:
            bFirstTokenFound = token_is_open_paren(oToken)

    return True


def second_open_paren_detected_after_first_open_paren_was_closed(bFirstTokenFound, iParen, oToken):
    if bFirstTokenFound:
        if iParen == 0 and token_is_open_paren(oToken):
            return True
    return False


def open_paren_after_assignment_operator(assignment_operator, lTokens):
    iToken = get_index_of_token_in_list(assignment_operator, lTokens)
    return is_next_token_ignoring_whitespace(parser.open_parenthesis, iToken, lTokens)


def open_paren_after_assignment_operator_is_aggregate(assignment_operator, lTokens):
    iToken = get_index_of_token_in_list(assignment_operator, lTokens)
    if is_next_token_ignoring_whitespace(parser.open_parenthesis, iToken, lTokens):
        iIndex = get_index_of_token_in_list_after_index(parser.open_parenthesis, lTokens, iToken)
        return isinstance(lTokens[iIndex], token.aggregate.open_parenthesis)
    return False


def open_paren_after_assignment_operator_id_matches_last_paren_id(assignment_operator, lTokens):
    iToken = get_index_of_token_in_list(assignment_operator, lTokens)
    if is_next_token_ignoring_whitespace(parser.open_parenthesis, iToken, lTokens):
        iIndex = get_index_of_token_in_list(parser.open_parenthesis, lTokens)
        iOpenParenId = lTokens[iIndex].iId
    lTokens.reverse()
    if is_next_token_ignoring_whitespace(parser.close_parenthesis, 1, lTokens):
        iIndex = get_index_of_token_in_list(parser.close_parenthesis, lTokens)
        iCloseParenId = lTokens[iIndex].iId
    else:
        lTokens.reverse()
        return False
    lTokens.reverse()
    if iOpenParenId == iCloseParenId:
        return True
    return False


def open_paren_after_assignment_operator_is_followed_by_aggregate_open_parenthesis(assignment_operator, lTokens):
    iToken = get_index_of_token_in_list(assignment_operator, lTokens)
    if is_next_token_ignoring_whitespace(parser.open_parenthesis, iToken, lTokens):
        iIndex = get_index_of_token_in_list(parser.open_parenthesis, lTokens)
        return is_next_token_ignoring_whitespace(token.aggregate.open_parenthesis, iIndex + 1, lTokens)
    return False


def close_paren_detected_at_end_of_tokens(lTokens):
    lTokens.reverse()
    if is_next_token_ignoring_whitespace(parser.close_parenthesis, 1, lTokens):
        lTokens.reverse()
        return True
    lTokens.reverse()
    return False


def remove_tois_with_pragmas(lToi):
    lReturn = []
    for oToi in lToi:
        if not oToi.token_type_exists(token.pragma.pragma):
            lReturn.append(oToi)
    return lReturn


def get_index_of_matching_close_paren(iToken, lTokens):
    for iIndex in range(iToken, len(lTokens)):
        if isinstance(lTokens[iIndex], parser.close_parenthesis):
            if lTokens[iIndex].iId == lTokens[iToken].iId:
                return iIndex
    return None
