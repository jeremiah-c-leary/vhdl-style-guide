
from vsg import parser


def is_token_at_start_of_line(iIndex, oTokenMap):
    if oTokenMap.is_token_at_index(parser.carriage_return, iIndex - 1):
        return True
    if oTokenMap.is_token_at_index(parser.carriage_return, iIndex - 2) and oTokenMap.is_token_at_index(parser.whitespace, iIndex - 1):
        return True
    return False


def is_token_at_end_of_line(iIndex, oTokenMap):
    if oTokenMap.is_token_at_index(parser.carriage_return, iIndex + 1):
        return True
    if oTokenMap.is_token_at_index(parser.comment, iIndex + 1):
        return True
    if oTokenMap.is_token_at_index(parser.whitespace, iIndex + 1):
        if oTokenMap.is_token_at_index(parser.carriage_return, iIndex + 2):
            return True
        if oTokenMap.is_token_at_index(parser.comment, iIndex + 2):
            return True
    return False


def get_indexes_of_token_list(lTokens, oTokenMap):
    lReturn = []
    for oToken in lTokens:
        lReturn.extend(oTokenMap.get_token_indexes(oToken))

    lReturn.sort()

    return lReturn


def get_line_numbers_of_indexes_in_list(lIndexes, oTokenMap):
    lReturn = []
    for iIndex in lIndexes:
        lReturn.append(oTokenMap.get_line_number_of_index(iIndex))

    lReturn.sort()

    return lReturn


def is_index_between_indexes(iIndex, lStart, lEnd, bInclusive=False):
    for iStart, iEnd in zip(lStart, lEnd):
        if bInclusive:
            if iStart <= iIndex and iIndex <= iEnd:
                return True
        else:
            if iStart < iIndex and iIndex < iEnd:
                return True
    return False
