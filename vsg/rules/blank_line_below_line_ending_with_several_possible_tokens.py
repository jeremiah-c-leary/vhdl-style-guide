# -*- coding: utf-8 -*-

from vsg import parser, violation
from vsg.rules import (
    blank_line_below_line_ending_with_token as Rule,
    utils as rules_utils,
)


class blank_line_below_line_ending_with_several_possible_tokens(Rule):
    """
    Checks for a blank line below a line ending with a given token

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    token: token object type list
       token object that a blank line below should appear
    """

    def __init__(self, lTokens, lAllowTokens=None):
        super().__init__(lTokens, lAllowTokens)

    def _get_tokens_of_interest(self, oFile):
        if self.style.startswith("require_blank_line"):
            return oFile.get_line_below_line_ending_with_several_possible_tokens(self.lTokens)
        elif self.style == "no_blank_line":
            return oFile.get_blank_lines_below_line_ending_with_several_possible_tokens(self.lTokens)
