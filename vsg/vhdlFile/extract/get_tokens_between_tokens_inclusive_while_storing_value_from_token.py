
import bisect

from vsg.vhdlFile.extract import tokens


def get_tokens_between_tokens_inclusive_while_storing_value_from_token(left_token, right_token, value_token, lAllTokens, oTokenMap):

    lReturn = []

    lStart, lEnd = oTokenMap.get_token_pair_indexes(left_token, right_token)
#    print(lStart)
    lValueIndexes = oTokenMap.get_token_indexes(value_token)
#    print(lValueIndexes)
    iPreviousEnd = 0
    lValues = []
    lPopedValues = []
    for iStart, iEnd in zip(lStart, lEnd):
#        sValue = None
        push_value_index(lValueIndexes, lValues, lPopedValues, iStart) 
#        print('='*80)
#        print(f'iStart = {iStart}')
#        print(f'lValues = {lValues}')
#        print(f'lPopedValues = {lPopedValues}')

        try:
            oValueToken = lAllTokens[lValues[-1]]
            sValue = oValueToken.get_value()
        except IndexError:
            sValue = None
#        print(f'sValue = {sValue}')
 
        iLine = oTokenMap.get_line_number_of_index(iStart)

        oTokens = tokens.New(iStart, iLine, lAllTokens[iStart:iEnd + 1])
        oTokens.set_token_value(sValue)
        lReturn.append(oTokens)
        iPreviousEnd = iEnd
        try:
            lPopedValues.append(lValues.pop(-1))
        except IndexError:
            pass

    return lReturn


def push_value_index(lValueIndexes, lValues, lPopedValues, iLeftIndex):
    for iIndex, iValue in enumerate(lValueIndexes):
        if iLeftIndex > iValue and iValue not in lPopedValues and iValue not in lValues:
            lValues.append(iValue)
