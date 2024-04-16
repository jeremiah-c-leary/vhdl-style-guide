# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import (
    align_tokens_in_region_between_tokens_when_between_tokens_unless_between_tokens,
)

lAlign = []
lAlign.append(token.file_declaration.colon)
lAlign.append(token.signal_declaration.colon)
lAlign.append(token.constant_declaration.colon)
lAlign.append(token.variable_declaration.colon)
lAlign.append(token.alias_declaration.colon)
lAlign.append(token.alias_declaration.is_keyword)

oStartToken = token.if_generate_statement.generate_keyword
oEndToken = token.generate_statement_body.begin_keyword

lBetweenTokens = []
lBetweenTokens.append([token.if_generate_statement.if_keyword, token.if_generate_statement.end_keyword])

lUnless = []
lUnless.append([token.subprogram_body.is_keyword, token.subprogram_body.begin_keyword])


class rule_403(align_tokens_in_region_between_tokens_when_between_tokens_unless_between_tokens):
    """
    This rule checks the colons are in the same column for all declarations in the generate declarative part in if generate statements.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       signal sig1: natural;
       variable var2  : natural;
       constant c_period : time;
       file my_test_input : my_file_type;

    **Fix**

    .. code-block:: vhdl

       signal sig1        : natural;
       variable var2      : natural;
       constant c_period  : time;
       file my_test_input : my_file_type;
    """

    def __init__(self):
        super().__init__(lAlign, oStartToken, oEndToken, lBetweenTokens, lUnless)
        self.solution = "Align colon."
        self.subphase = 2
        self.configuration.remove("loop_control_statements_ends_group")
        self.configuration.remove("separate_generic_port_alignment")
