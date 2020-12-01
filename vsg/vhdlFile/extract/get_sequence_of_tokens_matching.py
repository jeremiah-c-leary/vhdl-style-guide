
from vsg.vhdlFile.extract import tokens
from vsg.vhdlFile.extract import utils


def get_sequence_of_tokens_matching(lTokens, lAllTokens, oTokenMap, bIgnoreIfLineStart=False):

    lReturn = []

    lIndexes = oTokenMap.get_token_indexes(lTokens[0])

    for iIndex in lIndexes:
        iLine = oTokenMap.get_line_number_of_index(iIndex)
        if bIgnoreIfLineStart and utils.is_token_at_start_of_line(iIndex, oTokenMap):
            continue
        for iToken, oToken in enumerate(lTokens):
            if not isinstance(lAllTokens[iToken + iIndex], oToken):
                break
        else:
            lReturn.append(tokens.New(iIndex, iLine, lAllTokens[iIndex:iIndex + len(lTokens)]))

    return lReturn
