# -*- coding: utf-8 -*-

lSingleCharacterSymbols = [",", ":", "(", ")", "'", '"', "+", "&", "-", "*", "/", "<", ">", ";", "=", "[", "]", "?"]
lTwoCharacterSymbols = ["=>", "**", ":=", "/=", ">=", "<=", "<>", "??", "?=", "?<", "?>", "<<", ">>", "--", "/*", "*/"]
lThreeCharacterSymbols = ["?/=", "?<=", "?>="]
lFourCharacterSymbols = ["\\?=\\"]

lStopChars = [" ", "(", ";"]


def create(sString):
    """
    This function takes a string and returns a list of tokens.
    """

    oLine = New(sString)
    oLine.combine_whitespace()
    oLine.combine_string_literals()
    oLine.combine_backslash_characters_into_symbols()
    oLine.combine_three_character_symbols()
    oLine.combine_two_character_symbols()
    oLine.combine_characters_into_words()
    oLine.combine_character_literals()
    oLine.split_natural_numbers()
    oLine.split_bit_string_literal_integer_and_base_specifier()
    return oLine.lChars


class New:
    def __init__(self, sLine):
        self.lChars = convert_string_to_chars(sLine)

    def combine_whitespace(self):
        lReturn = []
        sSpace = ""
        for sChar in self.lChars:
            if sChar.isspace():
                sSpace += sChar
            else:
                if sSpace.isspace():
                    lReturn.append(sSpace)
                    sSpace = ""
                lReturn.append(sChar)

        lReturn.append(sSpace)

        self.lChars = lReturn

    def combine_backslash_characters_into_symbols(self):
        lReturn = []
        sSymbol = ""
        bSymbol = False
        for sChar in self.lChars:
            if stop_character_found(sChar, bSymbol):
                bSymbol = False
                lReturn.append(sSymbol)
                sSymbol = ""
            bSymbol = inside_backslash_symbol(bSymbol, sChar)
            sSymbol = append_to_symbol(bSymbol, sSymbol, sChar)
            lReturn = append_to_list(bSymbol, lReturn, sChar)
        lReturn = add_trailing_string(lReturn, sSymbol)
        self.lChars = lReturn

    def combine_three_character_symbols(self):
        lReturn = []
        i = 0
        while i < len(self.lChars):
            sChars = "".join(self.lChars[i : i + 3])
            if sChars in lThreeCharacterSymbols:
                lReturn.append(sChars)
                i += 3
            else:
                lReturn.append(self.lChars[i])
                i += 1

        self.lChars = lReturn

    def combine_two_character_symbols(self):
        lReturn = []
        i = 0
        while i < len(self.lChars):
            sChars = "".join(self.lChars[i : i + 2])
            if sChars in lTwoCharacterSymbols:
                lReturn.append(sChars)
                i += 2
            else:
                lReturn.append(self.lChars[i])
                i += 1

        self.lChars = lReturn

    def combine_characters_into_words(self):
        lReturn = []
        sTemp = ""
        for sChar in self.lChars:
            if character_is_part_of_word(sChar):
                sTemp += sChar
            else:
                if sTemp != "":
                    lReturn.append(sTemp)
                lReturn.append(sChar)
                sTemp = ""

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

    def split_natural_numbers(self):
        lReturn = []
        for sChar in self.lChars:
            if is_natural_number(sChar):
                lReturn.extend(parse_natural_number(sChar))
            else:
                lReturn.append(sChar)

        self.lChars = lReturn

    def split_bit_string_literal_integer_and_base_specifier(self):
        lReturn = []
        iIndex = 0
        for iIndex, sChar in enumerate(self.lChars):
            sChar = self.lChars[iIndex]
            if is_bit_string_literal_integer_and_base_specifier(iIndex, self.lChars):
                lReturn.extend(parse_bit_string_literal_integer_and_base_specifier(sChar))
                continue
            lReturn.append(sChar)
        self.lChars = lReturn


def is_bit_string_literal_integer_and_base_specifier(iIndex, lChars):
    if iIndex < len(lChars) - 1:
        sChar = lChars[iIndex]
        sNextChar = lChars[iIndex + 1]
        if sChar.lower().endswith(("b", "o", "x", "d")) and sNextChar.startswith('"'):
            return True
        return False


def parse_bit_string_literal_integer_and_base_specifier(sIntegerAndBaseSpecifier):
    lReturn = []
    iSplitIndex = get_bit_string_literal_integer_and_base_specifier_split_index(sIntegerAndBaseSpecifier)
    lReturn.append(sIntegerAndBaseSpecifier[:iSplitIndex])
    lReturn.append(sIntegerAndBaseSpecifier[iSplitIndex:])
    lReturn = [x for x in lReturn if x != ""]
    return lReturn


def get_bit_string_literal_integer_and_base_specifier_split_index(sIntegerAndBaseSpecifier):
    for iIndex in range(len(sIntegerAndBaseSpecifier)):
        if not sIntegerAndBaseSpecifier[iIndex].isdigit():
            return iIndex


def is_natural_number(sString):
    lString = sString.lower().split("e")
    lBase = lString[0].split(".")
    lBase.extend(lString[1:])
    for sNum in lBase[0:-1]:
        if not sNum.isdigit():
            return False
    return True


def parse_natural_number(sString):
    lReturn = []
    sTemp = ""
    for sChar in sString:
        if sChar.lower() == "e":
            lReturn.append(sTemp)
            lReturn.append(sChar)
            sTemp = ""
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
        lReturn.append("".join(self.lChars[iLeft:iRight]))
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
    if (
        there_is_a_single_token_between_quotes(iIndex, lQuotes)
        and token_between_quotes_is_a_single_character(iQuote, lChars)
        and token_is_not_a_parenthesis(iQuote, lChars)
    ):
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


def token_is_not_a_parenthesis(iQuote, lChars):
    if lChars[iQuote + 1] == "(":
        return False
    return True


def filter_character_literal_candidates(lLiterals):
    lReturn = []
    for iIndex, lLiteral in enumerate(lLiterals[0:-1]):
        lNextLiteral = lLiterals[iIndex + 1]
        lPreviousLiteral = lLiterals[iIndex - 1]
        if lLiteral[1] == lNextLiteral[0] and lLiteral[0] == lPreviousLiteral[1]:
            continue
        lReturn.append(lLiteral)
    lReturn.append(lLiterals[-1])
    return lReturn


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
    if sChar == "\\":
        return True
    return False


def stop_character_found(sChar, bLiteral):
    if (sChar in lStopChars or " " in sChar) and bLiteral:
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
