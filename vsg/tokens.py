
lSingleCharacterSymbols = [',', ':', '(', ')', '\'', '"', '+', '&', '-', '*', '/', '<', '>', ';', '=', '[', ']', '?']
lTwoCharacterSymbols = ['=>','**', ':=', '/=', '>=', '<=', '<>', '??', '?=', '?<', '?>', '<<', '>>', '--']
lThreeCharacterSymbols = ['?/=', '?<', '?<=', '?>=']
lFourCharacterSymbols = ['\\?=\\']

lStopChars = [' ', '(', ';']


def create(sString):
    '''
    This function takes a string and returns a list of tokens.
    '''

    oLine = New(sString)
    oLine.combine_whitespace()
    oLine.combine_backslash_characters_into_symbols()
    oLine.combine_two_character_symbols()
    oLine.combine_characters_into_words()
    oLine.combine_string_literals()
    oLine.combine_character_literals()
    oLine.combine_comments()
    return oLine.lChars


class New():
    def __init__(self, sLine):
        self.lChars = convert_string_to_chars(sLine)

    def combine_whitespace(self):
        lReturn = []
        sSpace = ''
        for sChar in self.lChars:
            if sChar.isspace():
                sSpace += sChar
            else:
                if sSpace.isspace():
                    lReturn.append(sSpace)
                    sSpace = ''
                lReturn.append(sChar)

        lReturn.append(sSpace)

        self.lChars = lReturn

    def combine_backslash_characters_into_symbols(self):
        lReturn = []
        sSymbol = ''
        bSymbol = False
        for sChar in self.lChars:
            if stop_character_found(sChar, bSymbol):
                bSymbol = False
                lReturn.append(sSymbol)
                sSymbol = ''
            bSymbol = inside_backslash_symbol(bSymbol, sChar)
            sSymbol = append_to_symbol(bSymbol, sSymbol, sChar)
            lReturn = append_to_list(bSymbol, lReturn, sChar)
        lReturn = add_trailing_string(lReturn, sSymbol)
        self.lChars = lReturn

    def combine_two_character_symbols(self):
        lReturn = []
        sNextChar = ''
        bSkip = False
        for iChar, sChar in enumerate(self.lChars):
            if bSkip:
                bSkip = False
                continue
            try:
                sNextChar = self.lChars[iChar + 1]
            except IndexError:
                sNextChar = ''
            if sChar + sNextChar in lTwoCharacterSymbols:
                bSkip = True
                lReturn.append(sChar + sNextChar)
            else:
                lReturn.append(sChar)
        self.lChars = lReturn

    def combine_characters_into_words(self):
        lReturn = []
        sTemp = ''
        for sChar in self.lChars:
            if character_is_part_of_word(sChar):
                sTemp += sChar
            else:
                if sTemp != '':
                    lReturn.append(sTemp)
                lReturn.append(sChar)
                sTemp = ''

        if len(sTemp) != 0:
            lReturn.append(sTemp)

        self.lChars = lReturn

    def combine_string_literals(self):
        lQuotePairs = find_indexes_of_double_quote_pairs(self.lChars)
        lQuotePairs.reverse()

        for lPair in lQuotePairs:
            iLeft = lPair[0]
            iRight = lPair[1] + 1
            lReturn = self.lChars[0:iLeft]
            lReturn.append(''.join(self.lChars[iLeft:iRight]))
            lReturn.extend(self.lChars[iRight:])
            self.lChars = lReturn

    def combine_character_literals(self):
        lReturn = []
        sLiteral = ''
        bLiteral = False
        for iChar, sChar in enumerate(self.lChars):
            if sChar == "'" and not bLiteral:
                if not is_qualified_expression(iChar, self.lChars):
                    if is_character_literal(iChar, self.lChars):
                        sLiteral += sChar
                        bLiteral = True
                        continue
            if not bLiteral:
                lReturn.append(sChar)
            else:
                sLiteral += sChar
            if sChar == "'" and bLiteral:
                bLiteral = False
                lReturn.append(sLiteral)
                sLiteral = ''

        self.lChars = lReturn

    def combine_comments(self):
        if has_trailing_whitespace(self.lChars):
            combine_comment_with_trailing_whitespace(self)
        else:
            combine_comment(self)


def combine_comment_with_trailing_whitespace(self):
    if self.lChars.count('--') > 0:
        iIndex = self.lChars.index('--')
        lReturn = self.lChars[0:iIndex]
        lReturn.append(''.join(self.lChars[iIndex:-1]))
        lReturn.append(self.lChars[-1])
        self.lChars = lReturn


def combine_comment(self):
    if self.lChars.count('--') > 0:
        iIndex = self.lChars.index('--')
        lReturn = self.lChars[0:iIndex]
        lReturn.append(''.join(self.lChars[iIndex::]))
        self.lChars = lReturn


def combine_tokens_into_string(lTokens, iStart, iEnd):
    return ''.join(lTokens[iStart:iEnd])


def has_trailing_whitespace(lChars):
    if len(lChars) == 0:
        return False
    if lChars[-1].isspace():
        return True
    return False


def inside_backslash_symbol(bSymbol, sChar):
    if backslash_character_found(sChar):
        return True
    return bSymbol


def append_to_symbol(bSymbol, sSymbol, sChar):
    if bSymbol:
        return sSymbol + sChar
    return sSymbol


def append_to_list(bSymbol, lChars, sChar):
    lReturn = lChars
    if not bSymbol:
        lReturn.append(sChar)
    return lReturn


def backslash_character_found(sChar):
    if sChar == '\\':
        return True
    return False


def stop_character_found(sChar, bLiteral):
    if (sChar in lStopChars or ' ' in sChar) and bLiteral:
        return True
    return False


def add_trailing_string(lReturn, sString):
    if len(sString) > 0:
        lReturn.append(sString)
    return lReturn


def is_qualified_expression(iChar, lChars):
    lPattern = ["'", "(", "'"]
    try:
        if lChars[iChar:iChar + 3] == lPattern and len(lChars[iChar + 3]) == 1 and lChars[iChar + 4] == "'":
            return True
        return False
    except IndexError:
        return False


def is_character_literal(iChar, lChars):
    try:
        if lChars[iChar] == "'" and len(lChars[iChar + 1]) == 1 and lChars[iChar + 2] == "'":
            return True
        return False
    except IndexError:
        return False


def convert_string_to_chars(sString):
    lReturn = []
    for sChar in sString:
        lReturn.append(sChar)
    return lReturn


def append_character(sTemp, lReturn, sChar):
    if sTemp != '':
        lReturn.append(sTemp)
    lReturn.append(sChar)
    return lReturn, ''


def character_is_part_of_word(sChar):
    if len(sChar) > 1:
        return False
    elif sChar.isspace():
        return False
    elif sChar in lSingleCharacterSymbols:
        return False
    return True


def find_indexes_of_double_quote_pairs(lTokens):
    bStart = False
    lReturn = []
    for iToken, sToken in enumerate(lTokens):
        if sToken == '"' and bStart:
            lReturn.append([iStart, iToken]) 
            bStart = False
            continue
        if sToken == '"' and not bStart:
            iStart = iToken
            bStart = True
    return lReturn
