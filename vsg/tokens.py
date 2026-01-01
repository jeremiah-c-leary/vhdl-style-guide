# -*- coding: utf-8 -*-

lSingleCharacterSymbols = {",", ":", "(", ")", "'", '"', "+", "&", "-", "*", "/", "<", ">", ";", "=", "[", "]", "?"}
lTwoCharacterSymbols = {"=>", "**", ":=", "/=", ">=", "<=", "<>", "??", "?=", "?<", "?>", "<<", ">>", "--", "/*", "*/"}
lThreeCharacterSymbols = {"?/=", "?<=", "?>="}
lMultiCharacterSymbols = lTwoCharacterSymbols | lThreeCharacterSymbols

lStopChars = {" ", "(", ";"}


def build_symbol_prefix_tree(lSymbols):
    dPrefixTree = {}
    for sSymbol in lSymbols:
        dNode = dPrefixTree
        for oChar in sSymbol:
            # Return the branch of the prefix tree for this character, or create an empty branch if there isn't one.
            dNode = dNode.setdefault(oChar, {})
        # Use $ as the marker for the end of a branch.
        dNode["$"] = sSymbol
    return dPrefixTree


dSymbolTree = build_symbol_prefix_tree(lMultiCharacterSymbols)


def create(sString):
    """
    This function takes a string and returns a list of tokens.
    """

    oLine = New(sString)
    oLine.combine_whitespace()
    oLine.combine_string_literals()
    oLine.combine_backslash_characters_into_symbols()
    oLine.combine_symbols_with_prefix_tree()
    oLine.combine_characters_into_words()
    oLine.combine_character_literals()
    oLine.split_natural_numbers()
    oLine.split_bit_string_literal_integer_and_base_specifier()
    return oLine.lChars


class New:
    def __init__(self, sLine):
        self.lChars = list(sLine)

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

    def combine_symbols_with_prefix_tree(self):
        lReturn = []
        iStart = 0
        iNumChars = len(self.lChars)
        while iStart < iNumChars:
            dNode = dSymbolTree
            iEnd = iStart
            oLastMatch = None
            iPrevEnd = iStart
            # Try to match as long a symbol as possible.
            while iEnd < iNumChars and self.lChars[iEnd] in dNode:
                dNode = dNode[self.lChars[iEnd]]
                iEnd += 1
                if "$" in dNode:
                    oLastMatch = dNode["$"]
                    iPrevEnd = iEnd
            if oLastMatch:
                lReturn.append(oLastMatch)
                iStart = iPrevEnd
            else:
                lReturn.append(self.lChars[iStart])
                iStart += 1
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

    def combine_characters_into_words(self):
        lReturn = []
        sWord = []

        for sChar in self.lChars:
            if character_is_part_of_word(sChar):
                sWord.append(sChar)
            else:
                if sWord:
                    lReturn.append("".join(sWord))
                    sWord.clear()
                lReturn.append(sChar)

        if sWord:
            lReturn.append("".join(sWord))

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
    return (
        there_is_a_single_token_between_quotes(iIndex, lQuotes)
        and token_between_quotes_is_a_single_character(iQuote, lChars)
        and token_is_not_a_parenthesis(iQuote, lChars)
    )


def there_is_a_single_token_between_quotes(iIndex, lQuotes):
    return lQuotes[iIndex] + 2 == lQuotes[iIndex + 1]


def token_between_quotes_is_a_single_character(iQuote, lChars):
    return len(lChars[iQuote + 1]) == 1


def token_is_not_a_parenthesis(iQuote, lChars):
    return lChars[iQuote + 1] == "("


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
    return sChar == "\\"


def stop_character_found(sChar, bLiteral):
    return (sChar in lStopChars or " " in sChar) and bLiteral


def add_trailing_string(lReturn, sString):
    if len(sString) > 0:
        lReturn.append(sString)
    return lReturn


def character_is_part_of_word(sChar):
    return len(sChar) == 1 and not sChar.isspace() and sChar not in lSingleCharacterSymbols


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
