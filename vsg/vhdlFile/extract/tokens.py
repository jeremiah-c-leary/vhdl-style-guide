
from vsg import parser


class New():

    def __init__(self, iStartIndex, iLine, lTokens):

        self.iStartIndex = iStartIndex
        self.lTokens = lTokens
        self.iLine = iLine
        self.sTokenValue = None
        try:
            self.iEndIndex = iStartIndex + len(lTokens)
        except TypeError:
            self.iEndIndex = None

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
        lTokens = self.lTokens[iStart:iEnd + 1]
        iStartIndex = iStart + self.iStartIndex
        iLine = self.iLine
        for iIndex in range(0, iStart + 1):
            if isinstance(self.lTokens[iIndex], parser.carriage_return):
                iLine += 1
        return New(iStartIndex, iLine, lTokens)

    def get_start_index(self):
        return self.iStartIndex

    def get_end_index(self):
        return self.iEndIndex
