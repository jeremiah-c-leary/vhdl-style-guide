# -*- coding: utf-8 -*-

import bisect

from vsg import parser
from vsg.vhdlFile.extract import tokens


def get_line_preceding_line(iLine, lAllTokens, iNumLines, oTokenMap, bSkipComments=False):
    lCarriageReturns = oTokenMap.get_token_indexes(parser.carriage_return)

    if not bSkipComments:
        iAdjust = -2
        iStartIndex = iLine - iNumLines + iAdjust
        if iStartIndex < 0:
            iStart = 0
        else:
            iStart = lCarriageReturns[iStartIndex] + 1
        iEnd = lCarriageReturns[iLine + iAdjust]
        lTemp = lAllTokens[iStart:iEnd]
        return tokens.New(iStart, iLine, lTemp)
    else:
        iStartIndex = _get_start_index(lCarriageReturns, iLine, oTokenMap)

        if iStartIndex == 0:
            iTokenStartIndex = 0
            iTokenEndIndex = lCarriageReturns[iTokenStartIndex]
        else:
            iTokenStartIndex = lCarriageReturns[iStartIndex - 1] + 1
            iTokenEndIndex = lCarriageReturns[iStartIndex]

        iLine = iStartIndex + 2
        lTokens = lAllTokens[iTokenStartIndex:iTokenEndIndex]
        return tokens.New(iTokenStartIndex, iLine, lTokens)


def _build_index_list(oTokenMap):
    lTemp = oTokenMap.get_token_indexes(parser.comment).copy()
    lTemp.extend(oTokenMap.get_token_indexes(parser.whitespace).copy())
    lTemp.extend(oTokenMap.get_token_indexes(parser.carriage_return).copy())
    lTemp.sort()
    return lTemp


def _get_start_index(lCarriageReturns, iLine, oTokenMap):
    lTemp = _build_index_list(oTokenMap)
    iCurrent = lCarriageReturns[iLine - 2]
    iTempIndex = lTemp.index(iCurrent) - 1
    for i in range(iTempIndex, -1, -1):
        if lTemp[i] != iCurrent - 1:
            break
        iCurrent = lTemp[i]
    iStartIndex = bisect.bisect_left(lCarriageReturns, iCurrent)
    return iStartIndex
