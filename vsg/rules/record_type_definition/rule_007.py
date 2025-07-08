# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import move_token_left_to_next_non_whitespace_token as Rule
from vsg.vhdlFile import utils

lTokens = []

oLeft = token.full_type_declaration.type_keyword
oRight = token.full_type_declaration.semicolon
oToken = token.record_type_definition.record_keyword


class rule_007(Rule):
    """
    This rule checks the semicolon is on the same line as the **record** keyword.

    **Violation**

    .. code-block:: vhdl

       type t_record is record
         a : std_logic;
         b : std_logic;
       end record t_record
       ;

    **Fix**

    .. code-block:: vhdl

       type t_record is record
         a : std_logic;
         b : std_logic;
       end record t_record;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.bInsertWhitespace = False
        self.subphase = 3
        self.solution = "Move semicolon"

    def _get_tokens_of_interest(self, oFile):
        lReturn = []
        lToi = oFile.get_tokens_bounded_by_tokens_if_token_is_between_them(oLeft, oRight, oToken)
        for oToi in lToi:
            lTokens, iStartIndex, iLastIndex = extract_indexes(oToi)
            if tokens_are_on_same_line(lTokens, iStartIndex):
                continue
            if self.skip_based_on_whitespace(self.bInsertWhitespace, lTokens[iStartIndex::]):
                continue
            if utils.pragma_exists_in_tokens(lTokens, iStartIndex):
                continue
            lReturn.append(oToi.extract_tokens(iStartIndex, iLastIndex))
        return lReturn


def tokens_are_on_same_line(lTokens, iStartIndex):
    return len(lTokens[iStartIndex::]) == 2


def extract_indexes(oToi):
    lTokens = oToi.get_tokens()
    iLastIndex = oToi.get_length_of_tokens() - 1
    iStartIndex = utils.find_previous_non_whitespace_token(iLastIndex - 1, lTokens)
    return lTokens, iStartIndex, iLastIndex
