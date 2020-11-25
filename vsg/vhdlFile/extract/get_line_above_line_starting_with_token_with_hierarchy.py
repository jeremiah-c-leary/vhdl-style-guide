
from vsg import parser

from vsg.vhdlFile import utils

from vsg.vhdlFile import vhdlFile


def get_line_above_line_starting_with_token_with_hierarchy(lTokens, lAllTokens, lHierarchy):
    lReturn = []
    iLine = 1
    lPreviousLine = []
    iPrevious = 0
    lCurrentLine = []
    iCurrent = 0
    for iIndex in range(0, len(lAllTokens)):

        if isinstance(lAllTokens[iIndex], parser.carriage_return):
            iLine +=1
            lPreviousLine = lCurrentLine.copy()
            iPrevious = iCurrent
            lCurrentLine = []
            iCurrent = iIndex + 1
            for oToken in lTokens:
                if utils.are_next_consecutive_token_types([parser.whitespace, oToken], iCurrent, lAllTokens):
                    if lAllTokens[iIndex + 2].get_hierarchy() in lHierarchy:
                        lReturn.append(vhdlFile.Tokens(iPrevious, iLine, lPreviousLine))
                        break
                if utils.are_next_consecutive_token_types([oToken], iCurrent, lAllTokens):
                    if lAllTokens[iIndex + 1].get_hierarchy() in lHierarchy:
                        lReturn.append(vhdlFile.Tokens(iPrevious, iLine, lPreviousLine))
                        break
        else:
            lCurrentLine.append(lAllTokens[iIndex])

    return lReturn
