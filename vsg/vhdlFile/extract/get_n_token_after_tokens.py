
from vsg.vhdlFile.extract import tokens


def get_n_token_after_tokens(iToken, lTokens, lAllTokens, oTokenMap):
    lReturn = []
    lIndexes = []
    for oToken in lTokens:
        lTemp = oTokenMap.get_token_indexes(oToken)
        for iTemp in lTemp:
            iTokenIndex = iTemp
            for iCount in range(0, iToken):
                iTokenIndex = oTokenMap.get_index_of_next_non_whitespace_token(iTokenIndex, bExcludeComments=True)
            lIndexes.append(iTokenIndex)

    lIndexes.sort()

    for iIndex in lIndexes:
        iLine = oTokenMap.get_line_number_of_index(iIndex)
        lReturn.append(tokens.New(iIndex, iLine, [lAllTokens[iIndex]]))

    return lReturn
