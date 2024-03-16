# -*- coding: utf-8 -*-

from vsg.rules import align_tokens_in_region_between_tokens as Rule


class align_tokens_in_region_between_tokens_unless_between_tokens(Rule):
    """
    Aligns tokens in a region.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : token object list
       List of tokens to align

    left_token : token object
       The first token that defines the region

    right_token : token object
       The second token that defines the region

    lUnless : token object pairs list
       A list of pairs of tokens in which to exclude alignment
    """

    def __init__(self, lTokens, left_token, right_token, lUnless):
        super().__init__(lTokens=lTokens, left_token=left_token, right_token=right_token)
        self.lUnless = lUnless

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by_unless_between(self.left_token, self.right_token, self.lUnless)
