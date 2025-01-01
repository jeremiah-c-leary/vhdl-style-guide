# -*- coding: utf-8 -*-

from vsg import parser, token
from vsg.rules import utils
from vsg.rules.whitespace_after_token import Rule

lTokens = []
lTokens.append(token.interface_constant_declaration.assignment)
lTokens.append(token.interface_signal_declaration.assignment)
lTokens.append(token.interface_variable_declaration.assignment)
lTokens.append(token.interface_file_declaration.colon)
lTokens.append(token.interface_unknown_declaration.assignment)

oStart = token.generic_clause.open_parenthesis
oEnd = token.generic_clause.close_parenthesis

lUnless = []
lUnless.append([token.interface_function_specification.function_keyword, token.interface_function_specification.close_parenthesis])
lUnless.append([token.interface_procedure_specification.procedure_keyword, token.interface_procedure_specification.close_parenthesis])


class rule_006(Rule):
    """
    This rule checks for a single space after the default assignment.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       g_width : integer :=32;
       g_depth : integer :=     512;

    **Fix**

    .. code-block:: vhdl

       g_width : integer := 32;
       g_depth : integer := 512;
    """

    def __init__(self):
        super().__init__(lTokens)

    def _get_tokens_of_interest(self, oFile):
        lToi = oFile.get_token_and_n_tokens_after_it_when_between_tokens_unless_between_tokens(self.lTokens, 2, oStart, oEnd, lUnless)
        lToi = utils.remove_toi_if_token_is_at_the_end_of_the_line(lToi)
        return lToi
