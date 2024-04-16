# -*- coding: utf-8 -*-

from vsg.vhdlFile.extract import tokens


def get_line_count_between_tokens(oStart, oEnd, lAllTokens, oTokenMap):
    lReturn = []

    lStart, lEnd = oTokenMap.get_token_pair_indexes(oStart, oEnd)

    lStartLines = []
    lDeltaLines = []
    lStartIndexes = []
    for iStart, iEnd in zip(lStart, lEnd):
        iStartLine = oTokenMap.get_line_number_of_index(iStart)
        lStartLines.append(iStartLine)

        iEndLine = oTokenMap.get_line_number_of_index(iEnd)
        lDeltaLines.append(iEndLine - iStartLine)
        lStartIndexes.append(iStart)

    for iStart, iLine, iDelta, iStartIndex in zip(lStart, lStartLines, lDeltaLines, lStartIndexes):
        oTokens = tokens.New(None, iLine, [lAllTokens[iStartIndex]])
        oTokens.set_meta_data("length", iDelta)
        lReturn.append(oTokens)

    return lReturn
