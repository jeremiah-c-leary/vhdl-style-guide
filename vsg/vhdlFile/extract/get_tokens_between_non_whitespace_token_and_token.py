
import bisect

from vsg.vhdlFile.extract import tokens


def get_tokens_between_non_whitespace_token_and_token(right_token, lAllTokens, oTokenMap, sType="left"):

    lReturn = []

    lStart, lEnd = get_start_and_end_indexes(right_token, lAllTokens, oTokenMap, sType)

    for iStart, iEnd in zip(lStart, lEnd):
        if tokens_are_next_to_each_other(iStart, iEnd):
            continue

        iLine = oTokenMap.get_line_number_of_index(iStart)

        oTokens = tokens.New(iStart, iLine, lAllTokens[iStart:iEnd + 1])
        lReturn.append(oTokens)

    return lReturn


def get_start_and_end_indexes(right_token, lAllTokens, oTokenMap, sType):
    if sType=='left':
        lEnd = oTokenMap.get_token_indexes(right_token)
        lStart = []
        for iEnd in lEnd:
            lStart.append(oTokenMap.get_index_of_previous_non_whitespace_token(iEnd))
    else:
        lStart = oTokenMap.get_token_indexes(right_token)
        lEnd = []
        for iStart in lStart:
            lEnd.append(oTokenMap.get_index_of_next_non_whitespace_token_after_index_ignoring_comments(iStart))
    return lStart, lEnd


def tokens_are_next_to_each_other(iStart, iEnd):
    if iStart == iEnd - 1:
        return True
    return False
