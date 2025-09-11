# -*- coding: utf-8 -*-

from vsg.token import signal_declaration as token
from vsg.rules import multiline_alignment_between_tokens as Rule
from vsg.vhdlFile import utils

lTokenPairs = []
lTokenPairs.append([token.signal_keyword, token.semicolon])


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
        super().__init__(lTokenPairs)
        self.phase = 5
        self.subphase = 3
        self.bIgnoreStartParen = True
        self.bConstraint = True

    def _get_tokens_of_interest_list(self, oFile):

        oAssignmentToken = token.assignment_operator
        lReturn = []

        for lTokenPair in self.lTokenPairs:
            aToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1], bExcludeLastToken=self.bExcludeLastToken)
            for oToi in aToi:
                oAssignment = oToi.get_first_token_matching(oAssignmentToken)
                if oAssignment is not None:
                    aToi = oFile.get_tokens_bounded_by(lTokenPair[0], oAssignmentToken, bExcludeLastToken=self.bExcludeLastToken)

            lReturn = utils.combine_two_token_class_lists(lReturn, aToi)

        return lReturn
