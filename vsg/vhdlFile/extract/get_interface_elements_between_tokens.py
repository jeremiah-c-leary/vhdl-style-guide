
from vsg import parser
from vsg import token

from vsg.vhdlFile.extract import tokens


def get_interface_elements_between_tokens(oStart, oEnd, lAllTokens, oTokenMap):
    lReturn = []
    lStartIndexes, lEndIndexes = oTokenMap.get_token_pair_indexes(oStart, oEnd)

    for iStart, iEnd in zip(lStartIndexes, lEndIndexes):
        iLine = oTokenMap.get_line_number_of_index(iStart)
        lToi = lAllTokens[iStart + 1:iEnd + 1]

        bStore = False
        iLineNumber = None
        lTemp = []
        for iIndex in range(0, len(lToi)):
            oToken = lToi[iIndex]
            if not isinstance(oToken, parser.whitespace) and not isinstance(oToken, parser.carriage_return) and not isinstance(oToken, parser.comment) and not bStore:
                bStore = True
                iStartIndex = iIndex + iStart + 1
                iLineNumber = iLine

            if bStore:
               lTemp.append(lToi[iIndex])

            if isinstance(oToken, token.interface_list.semicolon):
                lTemp.pop()
                lReturn.append(tokens.New(iStartIndex, iLineNumber, lTemp))
                lTemp = []
                bStore = False

            if isinstance(lToi[iIndex], parser.carriage_return):
                iLine +=1

        if len(lTemp) > 0:
            lTemp.pop()
            for i in range(1, 5):
                if isinstance(lTemp[-1], parser.whitespace):
                    lTemp.pop()
                    continue
                if isinstance(lTemp[-1], parser.carriage_return):
                    lTemp.pop()
                    continue
                if isinstance(lTemp[-1], parser.comment):
                    lTemp.pop()
                    continue
            lReturn.append(tokens.New(iStartIndex, iLineNumber, lTemp))

    return lReturn
