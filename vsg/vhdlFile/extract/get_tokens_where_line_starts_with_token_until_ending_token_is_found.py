
from vsg.vhdlFile.extract import tokens
from vsg.vhdlFile.extract import utils


def get_tokens_where_line_starts_with_token_until_ending_token_is_found(start_token, stop_token, lAllTokens, oTokenMap):

    lReturn = []

    lStartIndexes = utils.filter_tokens_which_start_a_line(start_token, oTokenMap)

    lStopIndexes = []
    for iStartIndex in lStartIndexes:
        lStopIndexes.append(oTokenMap.get_index_of_token_after_index(stop_token, iStartIndex))

    for iStart, iStop in zip(lStartIndexes, lStopIndexes):
        iLine = oTokenMap.get_line_number_of_index(iStart)
        lTemp = lAllTokens[iStart:iStop + 1]
        lReturn.append(tokens.New(iStart, iLine, lTemp))

    return lReturn
