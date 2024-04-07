# -*- coding: utf-8 -*-

from vsg.rules import token_indent as Rule


class token_indent_unless_between_tokens(Rule):
    """
    Checks the indent of tokens.
    """

    def __init__(self, lTokens, lUnless):
        super().__init__(lTokens=lTokens)
        self.lUnless = lUnless

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_at_beginning_of_line_matching_unless_between_tokens(self.lTokens, self.lUnless)
