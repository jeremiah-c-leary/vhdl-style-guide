
import bisect

from vsg.vhdlFile.extract import tokens


def get_tokens_between_tokens_inclusive_while_storing_value_from_token(left_token, right_token, value_token, lAllTokens, oTokenMap):

    lReturn = []

    lStart, lEnd = oTokenMap.get_token_pair_indexes(left_token, right_token)

    lValueIndexes = oTokenMap.get_token_indexes(value_token)

    iPreviousEnd = 0
    for iStart, iEnd in zip(lStart, lEnd):
        sValue = None

        iValueIndex = bisect.bisect_left(lValueIndexes, iEnd) - 1
        if iValueIndex >= 0:
            iValue = lValueIndexes[iValueIndex]

            oValueToken = lAllTokens[iValue]
            if iValue < iPreviousEnd:
                sValue = None
            else:
                sValue = oValueToken.get_value()
        else:
            sValue = None

        iLine = oTokenMap.get_line_number_of_index(iStart)

        oTokens = tokens.New(iStart, iLine, lAllTokens[iStart:iEnd + 1])
        oTokens.set_token_value(sValue)
        lReturn.append(oTokens)
        iPreviousEnd = iEnd

    return lReturn
