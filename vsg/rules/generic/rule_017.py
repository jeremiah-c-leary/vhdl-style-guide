# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import (
    token_case_n_token_after_tokens_between_tokens_unless_between_tokens,
)

lTokens = []
lTokens.append(token.interface_constant_declaration.colon)
lTokens.append(token.interface_variable_declaration.colon)
lTokens.append(token.interface_signal_declaration.colon)
lTokens.append(token.interface_unknown_declaration.colon)

oStart = token.generic_clause.open_parenthesis
oEnd = token.generic_clause.close_parenthesis

lUnless = []
lUnless.append([token.interface_function_specification.function_keyword, token.interface_function_specification.close_parenthesis])
lUnless.append([token.interface_procedure_specification.procedure_keyword, token.interface_procedure_specification.close_parenthesis])


class rule_017(token_case_n_token_after_tokens_between_tokens_unless_between_tokens):
    """
    This rule checks the generic type has proper case if it is a VHDL keyword.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

      generic (
        g_width : STD_LOGIC := '0';
        g_depth : Std_logic := '1'
      );

    **Fix**

    .. code-block:: vhdl

      generic (
        g_width : std_logic := '0';
        g_depth : std_logic := '1'
      );
    """

    def __init__(self):
        super().__init__(1, lTokens, oStart, oEnd, lUnless, True)
        self.disabled = True
        self.groups.append("case::keyword")
