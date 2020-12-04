

from vsg import parser

from vsg.vhdlFile.extract import tokens

from vsg.vhdlFile.extract import utils


def get_consecutive_lines_starting_with_token_and_stopping_when_token_starting_line_is_found(search_token, stop_token, lAllTokens, oTokenMap):

    lReturn = []
    lSearchIndexes = utils.filter_indexes_which_start_a_line(search_token, oTokenMap)
    lStopIndexes = utils.filter_indexes_which_start_a_line(stop_token, oTokenMap)

    lCarriageReturns = oTokenMap.get_token_indexes(parser.carriage_return)

    lSearchLines = []
    for iSearchIndex in lSearchIndexes:
        iIndex = oTokenMap.get_line_number_of_index(iSearchIndex) - 2
        lSearchLines.append(lCarriageReturns[iIndex])

    lStopLines = []
    for iStopIndex in lStopIndexes:
        iIndex = oTokenMap.get_line_number_of_index(iStopIndex) - 2
        lStopLines.append(lCarriageReturns[iIndex])

    iStart = None
    for iIndex, iValue in enumerate(lCarriageReturns):
        if iValue in lStopLines:
            if iStart is not None:
                iLine = oTokenMap.get_line_number_of_index(iStart)
                iStopIndex = lStopLines.index(iValue)
                iEnd = lStopIndexes[iStopIndex] + 1
                lTemp = lAllTokens[iStart:iEnd]
                lReturn.append(tokens.New(iStart, iLine, lTemp))
                iStart = None

        if iValue in lSearchLines:
            if iStart is None:
                iStart = iValue + 1
        else:
            iStart = None

    return lReturn
