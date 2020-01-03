
lSingleCharacterSymbols = [',', ':', '(', ')', '\'', '"', '+', '&', '-', '*', '/', '<', '>']
lMultipleCharacterSymbols = [':=', '\=', '<=', '=>', '>=', '**']

def create(sString):
    '''
    This function takes a string and returns a list of tokens.
    '''
    lReturn = []
    sToken = ''
    fCommentFound = False
    fMultipleCharacterSymbolFound = False
    fLastChar = False
    for iIndex, sChar in enumerate(sString):
        if iIndex + 1 == len(sString):
            fLastChar = True
            sNextChar = ''
        else:
            sNextChar = sString[iIndex + 1]

        if len(sToken) == 0:
            sToken = sChar
            if sChar == '-' and sNextChar == '-':
                fCommentFound = True
                continue
            if sChar + sNextChar in lMultipleCharacterSymbols:
                fMultipleCharacterSymbolFound = True
                sToken = sChar
                continue
            if sChar in lSingleCharacterSymbols:
                lReturn.append(sToken)
                sToken = ''
        else:
            # Handle comments
            if sChar == '-' and sNextChar == '-':
                fCommentFound = True
                lReturn.append(sToken)
                sToken = ''
            if fCommentFound:
                sToken += sChar
                continue
            # Handle multiple character symbols
            if fMultipleCharacterSymbolFound:
                fMultipleCharacterSymbolFound = False
                sToken += sChar
                lReturn.append(sToken)
                sToken = ''
                continue
            if not fLastChar:
                if sChar + sNextChar in lMultipleCharacterSymbols:
                    fMultipleCharacterSymbolFound = True
                    lReturn.append(sToken)
                    sToken = sChar
                    continue
            if sChar in lSingleCharacterSymbols:
                lReturn.append(sToken)
                lReturn.append(sChar)
                sToken = ''
                continue
            # Handle consecutive spaces
            if sChar == ' ' and sToken[-1] == ' ':
                sToken += sChar
            if not sChar == ' ' and not sToken[-1] == ' ':
                sToken += sChar
            if sChar == ' ' and not sToken[-1] == ' ':
                lReturn.append(sToken)
                sToken = sChar
            if not sChar == ' ' and sToken[-1] == ' ':
                lReturn.append(sToken)
                sToken = sChar

    if not sToken == '': 
        lReturn.append(sToken)

    return lReturn
