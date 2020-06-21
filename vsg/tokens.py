
lSingleCharacterSymbols = [',', ':', '(', ')', '\'', '"', '+', '&', '-', '*', '/', '<', '>', ';', '=']
lMultipleCharacterSymbols = [':=', '/=', '<=', '=>', '>=', '**', '--']

def create(sString):
    '''
    This function takes a string and returns a list of tokens.
    '''
    lTokens = []
    lSeparators = []
    sToken = ''
    fCommentFound = False
    fMultipleCharacterSymbolFound = False
    fLastChar = False
    for iIndex, sChar in enumerate(sString):

        sToken += sChar
        # Set the previous character
        if iIndex > 0:
            sPrevChar = sString[iIndex - 1]
        else:
            sPrevChar = ''

        # Set the next character
        if iIndex + 1 == len(sString):
            fLastChar = True
            sNextChar = ''
        else:
            sNextChar = sString[iIndex + 1]

        # Check for comments
        if sToken == '--':
            fCommentFound = True
            if iIndex == 1:
                lSeparators.append('')
        if fCommentFound:
            continue

        # Check for single character symbols
        if sToken in lSingleCharacterSymbols:
            if sToken + sNextChar not in lMultipleCharacterSymbols:
                lTokens.append(sToken)
                sToken = ''
                if iIndex == 0:
                    lSeparators.append('')
                if not sNextChar == ' ' and iIndex + 1 < len(sString):
                    lSeparators.append('')
                continue

        # Check for double character symbols
        if sToken in lMultipleCharacterSymbols:
            lTokens.append(sToken)
            sToken = ''
            if not sString[iIndex - 2] == ' ':
                lSeparators.append('')
            continue

        # Handle consecutive spaces
        if sChar == ' ' and not sNextChar == ' ':
            lSeparators.append(sToken)
            sToken = ''
            continue

        if not sChar == ' ' and sNextChar == ' ':
            lTokens.append(sToken)
            sToken = ''
            continue

        if not sChar == ' ' and sNextChar in lSingleCharacterSymbols:
            if sToken + sNextChar not in lMultipleCharacterSymbols:
                lTokens.append(sToken)
                sToken = ''
                lSeparators.append('')
                continue

        if not sChar == ' ' and iIndex == 0:
            if sToken + sNextChar not in lMultipleCharacterSymbols and \
               sNextChar not in lSingleCharacterSymbols:
                lSeparators.append('')

    if not sToken == '': 
        lTokens.append(sToken)

    return lTokens, lSeparators
