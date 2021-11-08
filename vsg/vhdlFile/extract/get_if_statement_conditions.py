
from vsg.token import if_statement as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.extract import tokens


def get_if_statement_conditions(lAllTokens, oTokenMap, fRemoveWhitespace=True):
    lReturn = []

    lStart = oTokenMap.get_token_indexes(token.if_keyword, bCopy=True)
    lStart.extend(oTokenMap.get_token_indexes(token.elsif_keyword, bCopy=True))
    lStart.sort()

    lEnd = []
    for iStart in lStart:
        lEnd.append(oTokenMap.get_index_of_token_after_index(token.then_keyword, iStart))

    for iStart, iEnd in zip(lStart, lEnd):
        lTemp = lAllTokens[iStart + 1: iEnd]
        iStartIndex = iStart + 1
        if fRemoveWhitespace:
            iStartIndex, lTemp = utils.remove_leading_whitespace_and_comments(iStart, lTemp)
            lTemp = utils.remove_trailing_whitespace_and_comments(lTemp)

        iLine = oTokenMap.get_line_number_of_index(iStartIndex)

        lReturn.append(tokens.New(iStartIndex, iLine, lTemp))

    return lReturn
