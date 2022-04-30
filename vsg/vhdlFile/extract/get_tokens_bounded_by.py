
from vsg import parser

from vsg.vhdlFile.extract import tokens


def get_tokens_bounded_by(oStart, oEnd, lAllObjects, oTokenMap, include_trailing_whitespace=False, bExcludeLastToken=False, bIncludeTillEndOfLine=False, bIncludeTillBeginningOfLine=False):

    lReturn = []
    lStart, lEnd = oTokenMap.get_token_pair_indexes(oStart, oEnd)

    lCarriageReturns = oTokenMap.get_token_indexes(parser.carriage_return)

    lNewStart = []
    if bIncludeTillBeginningOfLine:
        for iStart in lStart:
            lNewStart.append(oTokenMap.get_index_of_carriage_return_before_index(iStart) + 1)
    else:
        lNewStart = lStart

    lNewEnd = []
    if bIncludeTillEndOfLine:
        for iEnd in lEnd:
            lNewEnd.append(oTokenMap.get_index_of_carriage_return_after_index(iEnd))
    else:
        lNewEnd = lEnd

    if bExcludeLastToken:
        lNewEnd = [x - 1 for x in lNewEnd]

    lWhiteSpace = oTokenMap.get_token_indexes(parser.whitespace)
    if include_trailing_whitespace:
        for iNewEnd, iIndex in enumerate(lNewEnd):
            if iIndex + 1 in lWhiteSpace:
                lNewEnd[iNewEnd] +=1
    elif not bIncludeTillEndOfLine:
        for iNewEnd, iIndex in enumerate(lNewEnd):
            if iIndex in lWhiteSpace:
                lNewEnd[iNewEnd] -= 1
            if lNewEnd[iNewEnd] in lCarriageReturns:
                lNewEnd[iNewEnd] -= 1

    for iStart, iEnd, iIndex in zip(lNewStart, lNewEnd, lEnd):
        lTemp = lAllObjects[iStart: iEnd + 1]
        iStartLine = oTokenMap.get_line_number_of_index(iStart)
        oToi = tokens.New(iStart, iStartLine, lTemp)
        oToi.set_token_value(iIndex - iStart)
        lReturn.append(oToi)

        oStart = lAllObjects[iStart]
        oEnd = lAllObjects[iEnd]

    return lReturn
