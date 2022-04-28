
import bisect

from vsg.vhdlFile.extract import tokens


def get_tokens_between_tokens_inclusive_while_storing_value_from_token(left_token, right_token, value_token, lAllTokens, oTokenMap):

    lReturn = []

    lStart, lEnd = oTokenMap.get_token_pair_indexes(left_token, right_token)

    lValueIndexes = oTokenMap.get_token_indexes(value_token)

    lValues = []
    lValuesPopped = []
    for iStart, iEnd in zip(lStart, lEnd):

        update_value_list(lValueIndexes, lValues, lValuesPopped, iStart)

        iLine = oTokenMap.get_line_number_of_index(iStart)

        oTokens = tokens.New(iStart, iLine, lAllTokens[iStart:iEnd + 1])
        sValue = get_matching_token_value(lValues, lAllTokens)
        oTokens.set_token_value(sValue)
        lReturn.append(oTokens)
        update_popped_list(lValuesPopped, lValues)

    return lReturn


def update_value_list(lValueIndexes, lValues, lValuesPopped, iLeftIndex):
    for iValue in lValueIndexes:
        if iLeftIndex > iValue and iValue not in lValuesPopped and iValue not in lValues:
            lValues.append(iValue)


def get_matching_token_value(lValues, lAllTokens):
    try:
        oValueToken = lAllTokens[lValues[-1]]
        return oValueToken.get_value()
    except IndexError:
        return None


def update_popped_list(lValuesPopped, lValues):
    try:
        lValuesPopped.append(lValues.pop(-1))
    except IndexError:
        pass
