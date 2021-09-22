
from vsg.vhdlFile.extract import tokens
from vsg.vhdlFile.extract import utils


def get_token_and_n_tokens_before_it_in_between_tokens_unless_token_is_found(lTokens, iTokens, oStart, oEnd, oStop, lAllTokens, oTokenMap):
    lReturn = []

    lIndexes = utils.filter_tokens_between_tokens_unless_token_exists_between_them(lTokens, oStart, oEnd, oStop, oTokenMap)

    for iIndex in lIndexes:
        iStart = iIndex - iTokens
        if iStart >= 0:
            iLine = oTokenMap.get_line_number_of_index(iStart)
            lReturn.append(tokens.New(iStart, iLine, lAllTokens[iStart:iIndex + 1]))

    return lReturn
