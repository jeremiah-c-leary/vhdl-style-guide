
lSingleCharacterSymbols = [',', ':', '(', ')', '\'', '"', '+']

def create(sString):
    '''
    This function takes a string and returns a list of tokens.
    '''
    lReturn = []
    sToken = ''
    fCommentFound = False
    for iIndex, sChar in enumerate(sString):
        if len(sToken) == 0:
            sToken = sChar
            if sChar == '-' and sString[iIndex + 1] == '-':
                fCommentFound = True
                continue
            if sChar in lSingleCharacterSymbols:
                lReturn.append(sToken)
                sToken = ''
        else:
            # Handle comments
            if sChar == '-' and sString[iIndex + 1] == '-':
                fCommentFound = True
                lReturn.append(sToken)
                sToken = ''
            if fCommentFound:
                sToken += sChar
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
