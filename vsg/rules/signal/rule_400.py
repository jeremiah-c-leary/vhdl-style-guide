# -*- coding: utf-8 -*-

from vsg.rules import multiline_alignment_between_tokens as Rule
from vsg.token import signal_declaration as token
from vsg.vhdlFile import utils

lTokenPairsIfNoAssignment = []
lTokenPairsIfNoAssignment.append([token.signal_keyword, token.semicolon])

lTokenPairsIfAssignment = []
lTokenPairsIfAssignment.append([token.signal_keyword, token.assignment_operator])


class rule_400(Rule):
    """
    This rule checks alignment of multiline constraints in signal declarations.

    |configuring_multiline_indent_rules_link|

    **Violation**

    .. code-block:: vhdl

       signal sig_a : my_record(
                element1(7 downto 0),
       element2(3 downto 0)
               );

    **Fix**

    .. code-block:: vhdl

       signal sig_a : my_record(
           element1(7 downto 0),
           element2(3 downto 0)
         );
    """

    def __init__(self):
        super().__init__(lTokenPairsIfNoAssignment)
        self.phase = 5
        self.subphase = 3
        self.bIgnoreStartParen = True
        self.bConstraint = True
        self.skip_array = False

    def _get_tokens_of_interest_list(self, oFile):
        lReturn = []

        for lTokenPair in self.lTokenPairs:
            aToi = self.get_tokens_within_bounds(lTokenPair, oFile)
            if declaration_contains_assignment_operator(aToi):
                aToi = self.get_tokens_within_bounds(lTokenPairsIfAssignment[0], oFile)

            lReturn = utils.combine_two_token_class_lists(lReturn, aToi)

        return lReturn

    def get_tokens_within_bounds(self, lTokenPair, oFile):
        return oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1], bExcludeLastToken=self.bExcludeLastToken)


def declaration_contains_assignment_operator(aToi):
    for oToi in aToi:
        oAssignment = oToi.get_first_token_matching(token.assignment_operator)
        if oAssignment is not None:
            return True
    return False
