

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

    bGroupDetected = False
    iPreviousIndex = 0
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





#from vsg import parser
#
#from vsg.vhdlFile.extract import tokens
#
#from vsg.vhdlFile import utils
#
#
#def get_consecutive_lines_starting_with_token_and_stopping_when_token_starting_line_is_found(search_token, stop_token, lAllTokens, oTokenMap):
#    iLine = 1
#    lTemp = []
#    lReturn = []
#    iStart = 0
#    bStore = False
#    bStop = False
#    iLineNumber = None
#    for iIndex in range(0, len(lAllTokens)):
#
#        if bStore:
#            lTemp.append(lAllTokens[iIndex])
#
#        if bStop and isinstance(lAllTokens[iIndex], stop_token):
#            oTokens = tokens.New(iStart, iLineNumber, lTemp)
#            lReturn.append(oTokens)
#            bStore = False
#            lTemp = []
#            bStop = False
#
#        if isinstance(lAllTokens[iIndex], parser.carriage_return):
#            iLine +=1
#            if not bStore:
#                if utils.are_next_consecutive_token_types([parser.whitespace, search_token], iIndex + 1, lAllTokens) or \
#                   utils.are_next_consecutive_token_types([search_token], iIndex + 1, lAllTokens):
#                       iStart = iIndex + 1
#                       bStore = True
#                       iLineNumber = iLine
#            else:
#                if not utils.are_next_consecutive_token_types([parser.whitespace, search_token], iIndex + 1, lAllTokens) and \
#                   not utils.are_next_consecutive_token_types([search_token], iIndex + 1, lAllTokens) and \
#                   not utils.are_next_consecutive_token_types([parser.whitespace, stop_token], iIndex + 1, lAllTokens) and \
#                   not utils.are_next_consecutive_token_types([stop_token], iIndex + 1, lAllTokens):
#                       bStore = False
#                       lTemp = []
#                if utils.are_next_consecutive_token_types([parser.whitespace, stop_token], iIndex + 1, lAllTokens) or \
#                   utils.are_next_consecutive_token_types([stop_token], iIndex + 1, lAllTokens):
#                    bStop = True
#
#    return lReturn
