
from vsg import parser

from vsg.vhdlFile.extract import tokens

import bisect
import copy


def get_line_preceeding_line(iLine, lAllTokens, iNumLines, oTokenMap, bSkipComments=False):
#    print('--> get_line_preceeding_line')
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
    #    print(f'{iLine} | {iStart} | {iEnd} | {lTemp}')
        return tokens.New(iStart, iLine, lTemp)
    else:
#        print(f'{iLine}')
        lTemp = oTokenMap.get_token_indexes(parser.comment).copy()
        lTemp.extend(oTokenMap.get_token_indexes(parser.whitespace).copy())
        lTemp.extend(lCarriageReturns.copy())
        lTemp.sort()
        iCRIndex = lCarriageReturns[iLine - 2] 
#        print(f'lCarraigeReturns = {lCarriageReturns}')
#        print(f'Index = {iCRIndex}')
#        print(f'lTemp            = {lTemp}')
        iTempIndex = lTemp.index(iCRIndex) - 1
#        print(f'iTempIndex = {iTempIndex}')
        iCurrent = iCRIndex
        for i in range(iTempIndex, -1, -1):
#            print(i)
#            print(f'lTemp[i] | {iCurrent - 1}')
            if lTemp[i] != iCurrent - 1:
                break
            iCurrent = lTemp[i]
#        print(f'iCurrent = {iCurrent}')
#        iStartIndex = lCarriageReturns.index(iCurrent)
        iStartIndex = bisect.bisect_left(lCarriageReturns, iCurrent)
#        print(f'iStartIndex = {iStartIndex}')
        if iStartIndex == 0:
            iTokenStartIndex = 0
            iTokenEndIndex = lCarriageReturns[iTokenStartIndex]
        else:
            iTokenStartIndex = lCarriageReturns[iStartIndex - 1] + 1
            iTokenEndIndex = lCarriageReturns[iStartIndex]
#        print(f'iTokenStartIndex = {iTokenStartIndex}')
#        print(f'iTokenEndIndex = {iTokenEndIndex}')
        iLine = iStartIndex + 2
        lTokens = lAllTokens[iTokenStartIndex:iTokenEndIndex]
        return tokens.New(iTokenStartIndex, iLine, lTokens)
