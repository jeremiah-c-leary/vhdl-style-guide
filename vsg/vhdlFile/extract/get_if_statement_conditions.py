
from vsg import parser
from vsg.token import if_statement as token

from vsg.vhdlFile import utils
from vsg.vhdlFile import vhdlFile

lStartTokens = []
lStartTokens.append(token.if_keyword)
lStartTokens.append(token.elsif_keyword)

lEndTokens = []
lEndTokens.append(token.then_keyword)


def get_if_statement_conditions(lAllTokens):
    iLine = 1
    lReturn = []
    bTokenFound = False
    for iIndex in range(0, len(lAllTokens)):
        for oToken in lEndTokens:
            if isinstance(lAllTokens[iIndex], oToken) and bTokenFound:
                bTokenFound = False
                iStartIndex, lTemp = utils.remove_leading_whitespace_and_comments(iStartIndex, lTemp)
                lTemp = utils.remove_trailing_whitespace_and_comments(lTemp)
                lReturn.append(vhdlFile.Tokens(iStartIndex, iLine, lTemp))
                break
        if bTokenFound:
            lTemp.append(lAllTokens[iIndex])
        for oToken in lStartTokens:
            if isinstance(lAllTokens[iIndex], oToken) and not bTokenFound:
                iStartIndex = iIndex
                lTemp = []
                bTokenFound = True
                break

        if isinstance(lAllTokens[iIndex], parser.carriage_return):
            iLine +=1

    return lReturn

