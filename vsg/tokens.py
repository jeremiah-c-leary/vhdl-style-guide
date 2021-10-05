
lSingleCharacterSymbols = [',', ':', '(', ')', '\'', '"', '+', '&', '-', '*', '/', '<', '>', ';', '=', '[', ']', '?']
lTwoCharacterSymbols = ['=>','**', ':=', '/=', '>=', '<=', '<>', '??', '?=', '?<', '?>', '<<', '>>', '--']
lThreeCharacterSymbols = ['?/=', '?<', '?<=', '?>=']


def create(sString):
    '''
    This function takes a string and returns a list of tokens.
    '''
    lCharacters = []

    for sChar in sString:
        lCharacters.append(sChar)
    lCharacters = combine_whitespace(lCharacters)
    lCharacters = combine_two_character_symbols(lCharacters)
    lCharacters = combine_characters_into_words(lCharacters)
    lCharacters = combine_string_literals(lCharacters)
    lCharacters = combine_character_literals(lCharacters)
    lCharacters = combine_comments(lCharacters)
#    print(lCharacters)
    return lCharacters


def combine_comments(lChars):
    lReturn = []
    sComment = ''
    bComment = False
    iEnd = len(lChars) - 1
    for iChar, sChar in enumerate(lChars):
#        print(f'|{sChar}|')
        if sChar.startswith('--') and not bComment:
            sComment += sChar
            bComment = True
            continue
        if not bComment:
            lReturn.append(sChar)
        else:
            if iChar == iEnd:
                if sChar.isspace():
                    lReturn.append(sComment)
                    lReturn.append(sChar)
                    bComment = False
                    continue

            sComment += sChar

    if bComment:
        lReturn.append(sComment)

    return lReturn


def combine_string_literals(lChars):
    lReturn = []
    sLiteral = ''
    bLiteral = False
    for iChar, sChar in enumerate(lChars):
        try:
            if sChar == '"' and not bLiteral and '"' in lChars[iChar + 1:]:
                sLiteral += sChar
                bLiteral = True
                continue
        except IndexError:
            break
        if not bLiteral:
            lReturn.append(sChar)
        else:
            sLiteral += sChar
        if sChar == '"' and bLiteral:
            bLiteral = False
            lReturn.append(sLiteral)
            sLiteral = ''

    return lReturn


def combine_character_literals(lChars):
    lReturn = []
    sLiteral = ''
    bLiteral = False
    for iChar, sChar in enumerate(lChars):
        try:
            if sChar == "'" and lChars[iChar + 2] == "'" and len(lChars[iChar + 1]) == 1 and not bLiteral and lChars[iChar + 1] != '(':
                sLiteral += sChar
                bLiteral = True
                continue
        except IndexError:
            pass
        if not bLiteral:
            lReturn.append(sChar)
        else:
            sLiteral += sChar
        if sChar == "'" and bLiteral:
            bLiteral = False
            lReturn.append(sLiteral)
            sLiteral = ''

    return lReturn


def combine_characters_into_words(lChars):
    lReturn = []
    sTemp = ''
    for sChar in lChars:
        if len(sChar) > 1:
            if sTemp != '':
                lReturn.append(sTemp)
            lReturn.append(sChar)
            sTemp = ''
        elif sChar == ' ':
            if sTemp != '':
                lReturn.append(sTemp)
            lReturn.append(sChar)
            sTemp = ''
        elif sChar in lSingleCharacterSymbols:
            if sTemp != '':
                lReturn.append(sTemp)
            lReturn.append(sChar)
            sTemp = ''
        else:
            sTemp += sChar

    if len(sTemp) != 0:
        lReturn.append(sTemp)

    return lReturn


def combine_whitespace(lChars):
    lReturn = []
    sSpace = ''
    for sChar in lChars:
        if sChar == ' ':
            sSpace += sChar
        else:
            if sSpace != '':
                lReturn.append(sSpace)
                sSpace = ''
            lReturn.append(sChar)

    if sSpace != '':
        lReturn.append(sSpace)

    return lReturn


def combine_two_character_symbols(lChars):
    lReturn = []
    sNextChar = ''
    bSkip = False
    for iChar, sChar in enumerate(lChars):
        if bSkip:
            bSkip = False
            continue
        try:
            sNextChar = lChars[iChar + 1]
        except IndexError:
            sNextChar = ''
        if sChar + sNextChar in lTwoCharacterSymbols:
            bSkip = True
            lReturn.append(sChar + sNextChar)
        else:
            lReturn.append(sChar)
    return lReturn
