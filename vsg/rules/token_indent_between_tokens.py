# -*- coding: utf-8 -*-

from vsg.rules import token_indent as Rule


class token_indent_between_tokens(Rule):
    """
    Checks the indent of tokens.
    """

    def __init__(self, lTokens, oStart, oEnd, bInclusive=False):
        super().__init__(lTokens=lTokens)
        self.oStart = oStart
        self.oEnd = oEnd
        self.bInclusive = bInclusive

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_at_beginning_of_line_matching_between_tokens(self.lTokens, self.oStart, self.oEnd, self.bInclusive)
