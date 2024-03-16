# -*- coding: utf-8 -*-

from vsg import parser, violation
from vsg.rules import token_prefix as Rule, utils as rules_utils


class token_prefix_between_tokens(Rule):
    """
    Checks the prefix for words between tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of parser object types
       object types to check the prefix

    lPrefixes : string list
       acceptable prefixes
    """

    def __init__(self, lTokens, oStart, oEnd):
        super().__init__(lTokens=lTokens)
        self.oStart = oStart
        self.oEnd = oEnd

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching_in_range_bounded_by_tokens(self.lTokens, self.oStart, self.oEnd)
