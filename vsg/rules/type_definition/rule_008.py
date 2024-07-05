# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import (
    split_line_at_token_if_on_same_line_as_token_if_token_pair_are_not_on_the_same_line,
)

oToken = token.enumeration_type_definition.close_parenthesis

oSameLineToken = token.enumeration_type_definition.enumeration_literal

lTokenPair = [token.full_type_declaration.type_keyword, token.full_type_declaration.semicolon]


class rule_008(split_line_at_token_if_on_same_line_as_token_if_token_pair_are_not_on_the_same_line):
    """
    This rule checks the closing parenthesis of multiline enumerated types is on its own line.

    **Violation**

    .. code-block:: vhdl

       type state_machine is (
         idle,
         write,
         read,
         done);

    **Fix**

    .. code-block:: vhdl

       type state_machine is (
         idle,
         write,
         read,
         done
       );
    """

    def __init__(self):
        super().__init__(oToken, oSameLineToken, lTokenPair)
        self.solution = "Move closing parenthesis to the next line."
