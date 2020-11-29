
from vsg import parser
from vsg.vhdlFile import vhdlFile as utils


def get_sequence_of_tokens_matching(lTokens, lAllTokens, oTokenMap, bIgnoreIfLineStart=False):

    lReturn = []

    lIndexes = oTokenMap.get_token_indexes(lTokens[0])

    for iIndex in lIndexes:
        iLine = oTokenMap.get_line_number_of_index(iIndex)
        if bIgnoreIfLineStart and is_token_at_start_of_line(iIndex, lAllTokens):
            continue
        for iToken, oToken in enumerate(lTokens):
            if not isinstance(lAllTokens[iToken + iIndex], oToken):
                break
        else:
            lReturn.append(utils.Tokens(iIndex, iLine, lAllTokens[iIndex:iIndex + len(lTokens)]))

    return lReturn


def is_token_at_start_of_line(iToken, lAllTokens):
    if isinstance(lAllTokens[iToken - 1], parser.whitespace) and isinstance(lAllTokens[iToken - 2], parser.carriage_return):
        return True
    if isinstance(lAllTokens[iToken - 1], parser.carriage_return):
        return True
    return False
