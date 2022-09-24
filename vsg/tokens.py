
lSingleCharacterSymbols = [',', ':', '(', ')', '\'', '"', '+', '&', '-', '*', '/', '<', '>', ';', '=', '[', ']', '?']
lTwoCharacterSymbols = ['=>','**', ':=', '/=', '>=', '<=', '<>', '??', '?=', '?<', '?>', '<<', '>>', '--', '/*', '*/']
lThreeCharacterSymbols = ['?/=', '?<', '?<=', '?>=']
lFourCharacterSymbols = ['\\?=\\']

lStopChars = [' ', '(', ';']


def create(sString):
    '''
    This function takes a string and returns a list of tokens.
    '''

    oLine = New(sString)
    oLine.combine_whitespace()
    oLine.combine_string_literals()
    oLine.combine_backslash_characters_into_symbols()
    oLine.combine_two_character_symbols()
    oLine.combine_characters_into_words()
    oLine.combine_character_literals()
    oLine.combine_comments()
    oLine.split_natural_numbers()
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

        combine_quote_pairs(lQuotePairs, self)

    def combine_character_literals(self):
        lQuotes = find_indexes_of_token_with_value("'", self.lChars)
        lLiterals = find_character_literal_candidates(lQuotes, self.lChars)
        if len(lLiterals) == 0:
            return None
        lQuotePairs = filter_character_literal_candidates(lLiterals)
        lQuotePairs.reverse()

        combine_quote_pairs(lQuotePairs, self)

    def combine_comments(self):
        if has_trailing_whitespace(self.lChars):
            combine_comment_with_trailing_whitespace(self)
        else:
            combine_comment(self)

    def split_natural_numbers(self):
        lReturn = []
        for sChar in self.lChars:
            if is_natural_number(sChar):
                lReturn.extend(parse_natural_number(sChar))
            else:
                lReturn.append(sChar)

        self.lChars = lReturn


def is_natural_number(sString):
    lString = sString.lower().split('e')
    lBase = lString[0].split('.')
    lBase.extend(lString[1:])
    for sNum in lBase[0:-1]:
        if not sNum.isdigit():
            return False
    return True


def parse_natural_number(sString):
    lReturn = []
    sTemp = ''
    for sChar in sString:
        if sChar.lower() == 'e':
            lReturn.append(sTemp)
            lReturn.append(sChar)
            sTemp = ''
        else:
            sTemp += sChar
    if len(sTemp) > 0:
        lReturn.append(sTemp)
    return lReturn


def combine_quote_pairs(lQuotePairs, self):
    for lPair in lQuotePairs:
        iLeft = lPair[0]
        iRight = lPair[1] + 1
        lReturn = self.lChars[0:iLeft]
        lReturn.append(''.join(self.lChars[iLeft:iRight]))
        lReturn.extend(self.lChars[iRight:])
        self.lChars = lReturn


def find_character_literal_candidates(lQuotes, lChars):
    lReturn = []
    for iIndex, iQuote in enumerate(lQuotes[0:-1]):
        if is_character_literal_candidate(iIndex, lQuotes, lChars):
            lReturn.append([iQuote, iQuote + 2])
    return lReturn


def is_character_literal_candidate(iIndex, lQuotes, lChars):
    iQuote = lQuotes[iIndex]
    if there_is_a_single_token_between_quotes(iIndex, lQuotes) and \
       token_between_quotes_is_a_single_character(iQuote, lChars):
        return True
    return False


def there_is_a_single_token_between_quotes(iIndex, lQuotes):
    if lQuotes[iIndex] + 2 == lQuotes[iIndex + 1]:
        return True
    return False


def token_between_quotes_is_a_single_character(iQuote, lChars):
    if len(lChars[iQuote + 1]) == 1:
        return True
    return False


def filter_character_literal_candidates(lLiterals):
    lReturn = []
    for iIndex, lLiteral in enumerate(lLiterals[0:-1]):
        lNextLiteral = lLiterals[iIndex + 1]
        if lLiteral[1] != lNextLiteral[0]:
            lReturn.append(lLiteral)
    lReturn.append(lLiterals[-1])
    return lReturn


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


def convert_string_to_chars(sString):
    lReturn = []
    for sChar in sString:
        lReturn.append(sChar)
    return lReturn


def character_is_part_of_word(sChar):
    if len(sChar) > 1:
        return False
    elif sChar.isspace():
        return False
    elif sChar in lSingleCharacterSymbols:
        return False
    return True


def find_indexes_of_double_quote_pairs(lTokens):
    lReturn = []
    lIndexes = find_indexes_of_token_with_value('"', lTokens)
    for iIndex in range(0, len(lIndexes) - 1, 2):
        lReturn.append([lIndexes[iIndex], lIndexes[iIndex + 1]])
    return lReturn


def find_indexes_of_token_with_value(sValue, lTokens):
    lReturn = []
    for iToken, sToken in enumerate(lTokens):
        if sToken == sValue:
            lReturn.append(iToken)
    return lReturn
