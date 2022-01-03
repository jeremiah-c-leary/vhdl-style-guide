
lSingleCharacterSymbols = [',', ':', '(', ')', '\'', '"', '+', '&', '-', '*', '/', '<', '>', ';', '=', '[', ']', '?']
lTwoCharacterSymbols = ['=>','**', ':=', '/=', '>=', '<=', '<>', '??', '?=', '?<', '?>', '<<', '>>', '--']
lThreeCharacterSymbols = ['?/=', '?<', '?<=', '?>=']
lFourCharacterSymbols = ['\\?=\\']


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


lStopChars = [' ', '(', ';']


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


class New():
    def __init__(self, sLine):
        self.lChars = convert_string_to_chars(sLine)

    def combine_whitespace(self):
        lReturn = [] 
        sSpace = ''
        for sChar in self.lChars:
            if sChar == ' ':
                sSpace += sChar
            else:
                if sSpace != '':
                    lReturn.append(sSpace)
                    sSpace = ''
                lReturn.append(sChar)

        if sSpace != '':
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

        self.lChars = lReturn


    def combine_string_literals(self):
        lReturn = []
        sLiteral = ''
        bLiteral = False
        for iChar, sChar in enumerate(self.lChars):
            try:
                if sChar == '"' and not bLiteral and '"' in self.lChars[iChar + 1:]:
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
        lReturn = []
        sComment = ''
        bComment = False
        iEnd = len(self.lChars) - 1
        for iChar, sChar in enumerate(self.lChars):
#            print(f'|{sChar}|')
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

        self.lChars = lReturn


def convert_string_to_chars(sString):
    lReturn = []
    for sChar in sString:
        lReturn.append(sChar)
    return lReturn

