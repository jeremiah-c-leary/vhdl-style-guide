
from vsg.vhdlFile.extract import tokens
from vsg.vhdlFile.extract import utils


def get_n_tokens_before_and_after_tokens_bounded_by_tokens(iToken, lTokens, lBetween, lAllTokens, oTokenMap):
    lReturn = []
    lIndexes = []

    lIndexes = utils.filter_tokens_between_tokens(lTokens, lBetween[0], lBetween[1], oTokenMap)

    for iIndex in lIndexes:
        iLine = oTokenMap.get_line_number_of_index(iIndex)
        lReturn.append(tokens.New(iIndex - iToken, iLine, lAllTokens[iIndex - iToken:iIndex + iToken + 1]))

    return lReturn
