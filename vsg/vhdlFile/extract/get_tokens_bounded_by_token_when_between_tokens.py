
from vsg import parser

from vsg.vhdlFile.extract import tokens


def get_tokens_bounded_by_token_when_between_tokens(oLeft, oRight, oStart, oEnd, lAllTokens, oTokenMap, include_trailing_whitespace=False):
    iLine = 1
    lTemp = []
    lReturn = []
    bStore = False
    bRightFound = False
    bSearch = False
    for iIndex in range(0, len(lAllTokens)):

        if isinstance(lAllTokens[iIndex], oStart):
            bSearch = True
        if isinstance(lAllTokens[iIndex], oEnd):
            bSearch = False

        if bSearch:
            if isinstance(lAllTokens[iIndex], oLeft):
                bStore = True
                iStart = iIndex
                iStartLine = iLine
            if bStore:
                lTemp.append(lAllTokens[iIndex])
            if bRightFound:
                if isinstance(lAllTokens[iIndex], parser.whitespace):
                    lReturn.append(tokens.New(iStart, iStartLine, lTemp))
                else:
                    lReturn.append(tokens.New(iStart, iStartLine, lTemp[:-1]))
                bRightFound = False
                lTemp = []
                bStore = False
            if isinstance(lAllTokens[iIndex], oRight) and bStore:
                if not include_trailing_whitespace:
                    lReturn.append(tokens.New(iStart, iStartLine, lTemp))
                    lTemp = []
                    bStore = False
                else:
                    bRightFound = True

        if isinstance(lAllTokens[iIndex], parser.carriage_return):
            iLine +=1

    return lReturn
