
import bisect

from vsg.vhdlFile.extract import tokens


def get_tokens_between_non_whitespace_token_and_token(right_token, lAllTokens, oTokenMap):

    lReturn = []

    lStart, lEnd = get_start_and_end_indexes(right_token, lAllTokens, oTokenMap)

    for iStart, iEnd in zip(lStart, lEnd):

        iLine = oTokenMap.get_line_number_of_index(iStart)

        oTokens = tokens.New(iStart, iLine, lAllTokens[iStart:iEnd + 1])
        lReturn.append(oTokens)

    return lReturn


def get_start_and_end_indexes(right_token, lAllTokens, oTokenMap):
    lEnd = oTokenMap.get_token_indexes(right_token)
    lStart = []
    for iEnd in lEnd:
        lStart.append(oTokenMap.get_index_of_previous_non_whitespace_token(iEnd))
    return lStart, lEnd

