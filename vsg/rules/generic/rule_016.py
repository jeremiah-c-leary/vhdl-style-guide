# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import (
    insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens_unless_between_tokens as Rule,
)

lTokens = []
lTokens.append(token.interface_list.semicolon)

lTokenPairs = []
lTokenPairs.append([token.generic_clause.open_parenthesis, token.generic_clause.close_parenthesis])

lUnless = []
lUnless.append([token.interface_function_specification.function_keyword, token.interface_function_specification.close_parenthesis])
lUnless.append([token.interface_procedure_specification.procedure_keyword, token.interface_procedure_specification.close_parenthesis])


class rule_016(Rule):
    """
    This rule checks for multiple generics defined on a single line.

    **Violation**

    .. code-block:: vhdl

      generic (
        g_width : std_logic := '0';g_depth : std_logic := '1'
      );

    **Fix**

    .. code-block:: vhdl

      generic (
        g_width : std_logic := '0';
        g_depth : std_logic := '1'
      );
    """

    def __init__(self):
        super().__init__(lTokens, lTokenPairs, lUnless)
        self.solution = "Move multiple generics to their own lines."
