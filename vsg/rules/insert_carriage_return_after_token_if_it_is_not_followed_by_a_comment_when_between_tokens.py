# -*- coding: utf-8 -*-

from vsg import parser, violation
from vsg.rule_group import structure
from vsg.rules import utils as rules_utils
from vsg.vhdlFile import utils


class insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens(structure.Rule):
    """
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    token : token object type
       The token to insert a carriage return after.

    oStart : token object type
       The starting token which defines the range

    oEnd : token object type
       The ending token which defines the range
    """

    def __init__(self, lTokens, lTokenPairs):
        super().__init__()
        self.lTokens = lTokens
        self.lTokenPairs = lTokenPairs
        self.configuration_documentation_link = None

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for lTokenPair in self.lTokenPairs:
            for oToken in self.lTokens:
                lToi_a = oFile.get_token_and_n_tokens_after_it_when_between_tokens([oToken], 2, lTokenPair[0], lTokenPair[1])
                lToi = utils.combine_two_token_class_lists(lToi, lToi_a)
        return lToi

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if utils.are_next_consecutive_token_types([parser.carriage_return], 1, lTokens):
                continue
            if utils.are_next_consecutive_token_types([parser.whitespace, parser.comment], 1, lTokens):
                continue
            if utils.are_next_consecutive_token_types([parser.comment, parser.carriage_return], 1, lTokens):
                continue
            if utils.are_next_consecutive_token_types([parser.whitespace, parser.carriage_return], 1, lTokens):
                continue
            else:
                self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        rules_utils.insert_carriage_return(lTokens, 1)
        oViolation.set_tokens(lTokens)
