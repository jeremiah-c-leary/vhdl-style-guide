
from vsg import parser

from vsg.vhdlFile.extract import tokens


def get_tokens_bounded_by_unless_between(oStart, oEnd, lUnless, lAllObjects, oTokenMap, include_trailing_whitespace=False, bExcludeLastToken=False, bIncludeTillEndOfLine=False, bIncludeTillBeginningOfLine=False):

    lReturn = []

    lStart, lEnd = oTokenMap.get_token_pair_indexes(oStart, oEnd)

    lUnlessStart, lUnlessEnd = get_unless_token_indexes(lUnless, oTokenMap)

    lStart, lEnd = filter_token_pairs(lStart, lEnd, lUnlessStart, lUnlessEnd)

    lNewStart = adjust_start_token(bIncludeTillBeginningOfLine, lStart, oTokenMap)

    lNewEnd = adjust_end_token(bIncludeTillEndOfLine, bExcludeLastToken, include_trailing_whitespace, lEnd, oTokenMap)

    for iStart, iEnd, iIndex in zip(lNewStart, lNewEnd, lEnd):
        lTemp = lAllObjects[iStart: iEnd + 1]
        iStartLine = oTokenMap.get_line_number_of_index(iStart)
        oToi = tokens.New(iStart, iStartLine, lTemp)
        oToi.set_token_value(iIndex - iStart)
        lReturn.append(oToi)

    return lReturn


def adjust_start_token(bIncludeTillBeginningOfLine, lStart, oTokenMap):
    lReturn = []
    if bIncludeTillBeginningOfLine:
        for iStart in lStart:
            lReturn.append(oTokenMap.get_index_of_carriage_return_before_index(iStart) + 1)
    else:
        lReturn = lStart
    return lReturn


def adjust_end_token(bIncludeTillEndOfLine, bExcludeLastToken, include_trailing_whitespace, lEnd, oTokenMap):
    lNewEnd = include_end_of_line(bIncludeTillEndOfLine, lEnd, oTokenMap)
    lNewEnd = exclude_last_token(bExcludeLastToken, lNewEnd)

    lCarriageReturns = oTokenMap.get_token_indexes(parser.carriage_return)

    lWhiteSpace = oTokenMap.get_token_indexes(parser.whitespace)

    if include_trailing_whitespace:
        for iNewEnd, iIndex in enumerate(lNewEnd):
            if iIndex + 1 in lWhiteSpace:
                lNewEnd[iNewEnd] += 1
    elif not bIncludeTillEndOfLine:
        for iNewEnd, iIndex in enumerate(lNewEnd):
            if iIndex in lWhiteSpace:
                lNewEnd[iNewEnd] -= 1
            if lNewEnd[iNewEnd] in lCarriageReturns:
                lNewEnd[iNewEnd] -= 1


    return lNewEnd


def include_end_of_line(bIncludeTillEndOfLine, lEnd, oTokenMap):
    lReturn = []
    if bIncludeTillEndOfLine:
        for iEnd in lEnd:
            lReturn.append(oTokenMap.get_index_of_carriage_return_after_index(iEnd))
    else:
        lReturn = lEnd
    return lReturn


def exclude_last_token(bExcludeLastToken, lNewEnd):
    if bExcludeLastToken:
        return [x - 1 for x in lNewEnd]
    else:
        return lNewEnd


def get_unless_token_indexes(lUnless, oTokenMap):
    lReturnStart = []
    lReturnEnd = []
    for unless in lUnless:
        lStart, lEnd = oTokenMap.get_token_pair_indexes(unless[0], unless[1])
        lReturnStart.extend(lStart)
        lReturnEnd.extend(lEnd)
    return lReturnStart, lReturnEnd


def filter_token_pairs(lStart, lEnd, lUnlessStart, lUnlessEnd):
    lReturnStart = []
    lReturnEnd = []
    for iStart, iEnd in zip(lStart, lEnd):
        if not indexes_between_indexes(iStart, iEnd, lUnlessStart, lUnlessEnd):
            lReturnStart.append(iStart)
            lReturnEnd.append(iEnd)
    return lReturnStart, lReturnEnd


def indexes_between_indexes(iStart, iEnd, lUnlessStart, lUnlessEnd):
    for iUnlessStart, iUnlessEnd in zip(lUnlessStart, lUnlessEnd):
        if iUnlessStart < iStart < iUnlessEnd and \
           iUnlessStart < iEnd < iUnlessEnd:
            return True
    return False
