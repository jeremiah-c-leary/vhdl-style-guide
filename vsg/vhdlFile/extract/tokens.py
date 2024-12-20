# -*- coding: utf-8 -*-

from vsg import parser


class New:
    def __init__(self, iStartIndex, iLine, lTokens):
        self.iStartIndex = iStartIndex
        self.lTokens = lTokens
        self.iLine = iLine
        self.sTokenValue = None
        self.iEndIndex = calculate_end_index(iStartIndex, lTokens)
        self.dMetaData = {}

    def get_tokens(self):
        return self.lTokens

    def set_tokens(self, lTokens):
        self.lTokens = lTokens

    def get_line_number(self):
        return self.iLine

    def set_token_value(self, sToken):
        self.sTokenValue = sToken

    def get_token_value(self):
        return self.sTokenValue

    def extract_tokens(self, iStart, iEnd):
        lTokens = self.lTokens[iStart : iEnd + 1]
        iStartIndex = iStart + self.iStartIndex
        iLine = self.iLine
        for iIndex in range(0, iStart):
            try:
                if isinstance(self.lTokens[iIndex], parser.carriage_return):
                    iLine += 1
            except IndexError:
                iLine = iLine
        oToi = New(iStartIndex, iLine, lTokens)
        oToi.sTokenValue = self.sTokenValue
        oToi.dMetaData = self.dMetaData
        return oToi

    def get_start_index(self):
        return self.iStartIndex

    def get_end_index(self):
        return self.iEndIndex

    def does_first_token_match(self, oTokenType):
        return isinstance(self.lTokens[0], oTokenType)

    def get_first_token_matching(self, oTokenType):
        for oToken in self.lTokens:
            if isinstance(oToken, oTokenType):
                return oToken
        return None

    def token_type_exists(self, oTokenType):
        for oToken in self.lTokens:
            if isinstance(oToken, oTokenType):
                return True
        return False

    def set_meta_data(self, sKey, sValue):
        self.dMetaData[sKey] = sValue

    def get_meta_data(self, sKey):
        return self.dMetaData[sKey]

    def get_index_of_token_matching(self, oTokenType):
        for iToken, oToken in enumerate(self.lTokens):
            if isinstance(oToken, oTokenType):
                return iToken
        return None

    def get_index_of_last_token_matching(self, oTokenType):
        iReturn = None
        for iToken, oToken in enumerate(self.lTokens):
            if isinstance(oToken, oTokenType):
                iReturn = iToken
        return iReturn

    def extract_token_and_n_tokens_before_it(self, oTokenType, iNum):
        iEnd = self.get_index_of_token_matching(oTokenType)
        if iEnd is None:
            return None
        iStart = iEnd - iNum
        return self.extract_tokens(iStart, iEnd)


def calculate_end_index(iStartIndex, lTokens):
    try:
        iReturn = iStartIndex
        for oToken in lTokens:
            if not isinstance(oToken, parser.beginning_of_file):
                iReturn += 1
        return iReturn
    except TypeError:
        return None
