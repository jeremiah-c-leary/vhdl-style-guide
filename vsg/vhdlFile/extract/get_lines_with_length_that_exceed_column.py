
from vsg import parser

from vsg.vhdlFile import utils

from vsg.vhdlFile.extract import tokens


def get_lines_with_length_that_exceed_column(iColumn, lAllTokens, oTokenMap):
    iLine = 1
    lReturn = []
    lTemp = []
    bFirstTokenInLine = False
    for iIndex in range(0, len(lAllTokens)):

        if isinstance(lAllTokens[iIndex], parser.carriage_return):
            if utils.does_length_of_tokens_exceed(lTemp, iColumn):
                lReturn.append(tokens.New(iStart, iLine, lTemp))
            iLine +=1
            lTemp = []
            bFirstTokenInLine = True
            continue

        lTemp.append(lAllTokens[iIndex])
        if bFirstTokenInLine:
            iStart = iIndex

    return lReturn
