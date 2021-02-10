
from vsg.vhdlFile.extract import tokens


def get_tokens_bounded_by_tokens_if_token_is_between_them(oStart, oEnd, oToken, lAllObjects, oTokenMap):

    lReturn = []

    lStart, lEnd = oTokenMap.get_token_pair_indexes(oStart, oEnd)

    lIndexes = oTokenMap.get_token_indexes(oToken)

    for iStart, iEnd in zip(lStart, lEnd):
        for iIndex in lIndexes:
            if iStart < iIndex and iIndex < iEnd:
                lTemp = lAllObjects[iStart: iEnd + 1]
                iStartLine = oTokenMap.get_line_number_of_index(iStart)
                oToi = tokens.New(iStart, iStartLine, lTemp)
                oToi.set_token_value(iIndex - iStart)
                lReturn.append(oToi)

    return lReturn
