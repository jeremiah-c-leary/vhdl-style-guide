
from vsg.vhdlFile.extract import tokens


def get_line_count_between_tokens(oStart, oEnd, lAllTokens, oTokenMap):
    lReturn = []

    lStart, lEnd = oTokenMap.get_token_pair_indexes(oStart, oEnd)

    lStartLines = []
    lDeltaLines = []
    for iStart, iEnd in zip(lStart, lEnd):
        iStartLine = oTokenMap.get_line_number_of_index(iStart)
        lStartLines.append(iStartLine)

        iEndLine = oTokenMap.get_line_number_of_index(iEnd)
        lDeltaLines.append(iEndLine - iStartLine)

    for iStart, iLine, iDelta in zip(lStart, lStartLines, lDeltaLines):
        oTokens = tokens.New(None, iLine, [])
        oTokens.set_token_value(iDelta)
        lReturn.append(oTokens)

    return lReturn
