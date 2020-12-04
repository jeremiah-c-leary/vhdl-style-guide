
from vsg.vhdlFile.extract import tokens


def get_sequence_of_tokens_not_matching(lTokens, lAllTokens, oTokenMap):

    lReturn = []
    lIndexes = oTokenMap.get_token_indexes(lTokens[0])

    for iIndex in lIndexes:
        for i in range(1, len(lTokens)):
            if not oTokenMap.is_token_at_index(lTokens[i], iIndex + i):
                iLine = oTokenMap.get_line_number_of_index(iIndex)
                lReturn.append(tokens.New(iIndex, iLine, lAllTokens[iIndex:iIndex + 1]))
                break
    return lReturn
