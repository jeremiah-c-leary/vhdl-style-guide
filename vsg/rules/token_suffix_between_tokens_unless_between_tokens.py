# -*- coding: utf-8 -*-

from vsg import violation
from vsg.rules import token_suffix as Rule


class token_suffix_between_tokens_unless_between_tokens(Rule):
    """
    Checks the suffix of a token.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of parser object types
       object types to check the prefix

    lSuffixes: string list
       acceptable suffixes
    """

    def __init__(self, lTokens, oStart, oEnd, lUnless):
        super().__init__(lTokens=lTokens)
        self.oStart = oStart
        self.oEnd = oEnd
        self.lUnless = lUnless

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching_in_range_bounded_by_tokens_unless_between_tokens(self.lTokens, self.oStart, self.oEnd, self.lUnless)
