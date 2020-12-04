
from vsg import parser
from vsg import token

from vsg.vhdlFile.extract import tokens


def get_association_elements_between_tokens(oStart, oEnd, lAllTokens, oTokenMap):
    lReturn = []
    lStartIndexes, lEndIndexes = oTokenMap.get_token_pair_indexes(oStart, oEnd)

    for iStart, iEnd in zip(lStartIndexes, lEndIndexes):
        iLine = oTokenMap.get_line_number_of_index(iStart)
        lTokens = lAllTokens[iStart:iEnd + 1]

        bStore = False
        iLineNumber = None
        lTemp = []
        for iToken, oToken in enumerate(lTokens):
            if isinstance(oToken, token.association_element.formal_part):
                bStore = True
                iStartIndex = iToken + iStart
                iLineNumber = iLine
            if isinstance(oToken, token.association_element.actual_part) and not bStore:
                bStore = True
                iStartIndex = iToken + iStart
                iLineNumber = iLine

            if bStore:
               lTemp.append(oToken)

            if isinstance(oToken, token.association_list.comma):
                lReturn.append(tokens.New(iStartIndex, iLineNumber, lTemp))
                lTemp = []
                bStore = False

            if isinstance(oToken, parser.carriage_return):
                iLine +=1

        if len(lTemp) > 0:
            lReturn.append(tokens.New(iStartIndex, iLineNumber, lTemp))

    return lReturn
