
from vsg import parser

from vsg.vhdlFile import utils

from vsg.vhdlFile import vhdlFile as vutils


def get_blank_lines_above_line_starting_with_token(lTokens, lAllTokens):
    lReturn = []
    iLine = 1
    bStore = False
    lTemp = []
    iStart = 0
    for iIndex in range(0, len(lAllTokens)):

        if isinstance(lAllTokens[iIndex], parser.blank_line):
            if not bStore:
                iStart = iIndex
            bStore = True

        if bStore:
            lTemp.append(lAllTokens[iIndex])

        if isinstance(lAllTokens[iIndex], parser.carriage_return):
            iLine +=1
            iCurrent = iIndex + 1
            for oToken in lTokens:
                if utils.are_next_consecutive_token_types([parser.whitespace, oToken], iCurrent, lAllTokens):
                    lReturn.append(vutils.Tokens(iStart, iLine, lTemp))
                    break
                if utils.are_next_consecutive_token_types([oToken], iCurrent, lAllTokens):
                    lReturn.append(vutils.Tokens(iStart, iLine, lTemp))
                    break

            if not utils.are_next_consecutive_token_types([parser.blank_line, parser.carriage_return], iCurrent, lAllTokens):
                bStore = False
                lTemp = []

    return lReturn
