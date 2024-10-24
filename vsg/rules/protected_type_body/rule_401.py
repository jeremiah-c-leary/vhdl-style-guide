# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import (
    align_tokens_in_region_between_tokens_unless_between_tokens as Rule,
)

lAlign = []
lAlign.append(token.file_declaration.colon)
lAlign.append(token.signal_declaration.colon)
lAlign.append(token.constant_declaration.colon)
lAlign.append(token.variable_declaration.colon)
lAlign.append(token.alias_declaration.colon)
lAlign.append(token.alias_declaration.is_keyword)

oStart = token.protected_type_body.body_keyword
oEnd = token.protected_type_body.end_body_keyword

lUnless = []
lUnless.append([token.subprogram_body.is_keyword, token.subprogram_body.begin_keyword])


class rule_401(Rule):
    """
    This rule checks the colons are in the same column for all declarations in the protected type body declarative part.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       type my_type protected body is

         signal   wr_en : std_logic;
         signal   rd_en   : std_logic;
         constant c_period : time;

       end protected body;

    **Fix**

    .. code-block:: vhdl

       type my_type protected body is

         signal   wr_en    : std_logic;
         signal   rd_en    : std_logic;
         constant c_period : time;

       end protected body;
    """

    def __init__(self):
        super().__init__(lAlign, oStart, oEnd, lUnless)
        self.solution = "Align colon."
        self.subphase = 3
        self.configuration.remove("separate_generic_port_alignment")
        self.configuration.remove("if_control_statements_ends_group")
        self.configuration.remove("case_control_statements_ends_group")
        self.configuration.remove("loop_control_statements_ends_group")
