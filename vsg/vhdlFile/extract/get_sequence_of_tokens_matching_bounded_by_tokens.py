
from vsg.vhdlFile.extract import tokens


def get_sequence_of_tokens_matching_bounded_by_tokens(lTokens, oStart, oEnd, lAllTokens, oTokenMap):

    lReturn = []

    lStart = oTokenMap.get_token_indexes(oStart)
    lEnd = oTokenMap.get_token_indexes(oEnd)
    lIndexes = []
    for iStart, iEnd in zip(lStart, lEnd):
        lIndexes.extend(oTokenMap.get_token_indexes_between_indexes(lTokens[0], iStart, iEnd))

    lIndexes.sort()

    for iIndex in lIndexes:
        iLine = oTokenMap.get_line_number_of_index(iIndex)
        for iToken, oToken in enumerate(lTokens):
            if not isinstance(lAllTokens[iToken + iIndex], oToken):
                break
        else:
            lReturn.append(tokens.New(iIndex, iLine, lAllTokens[iIndex:iIndex + len(lTokens)]))

    return lReturn
