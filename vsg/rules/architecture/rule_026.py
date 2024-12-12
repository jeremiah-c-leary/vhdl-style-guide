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

lUnless = []
lUnless.append([token.subprogram_body.is_keyword, token.subprogram_body.begin_keyword])
lUnless.append([token.protected_type_body.body_keyword, token.protected_type_body.end_body_keyword])


class rule_026(Rule):
    """
    This rule checks the colons are in the same column for all declarations in the architecture declarative part.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       architecture rtl of my_entity is

         signal   wr_en : std_logic;
         signal   rd_en   : std_logic;
         constant c_period : time;

       begin

    **Fix**

    .. code-block:: vhdl

       architecture rtl of my_entity is

         signal   wr_en    : std_logic;
         signal   rd_en    : std_logic;
         constant c_period : time;

       begin
    """

    def __init__(self):
        super().__init__(lAlign, token.architecture_body.is_keyword, token.architecture_body.begin_keyword, lUnless)
        self.solution = "Align identifier."
        self.subphase = 3
        self.configuration.append("include_type_is_keyword")
        self.is_keyword = token.full_type_declaration.is_keyword
        self.configuration.remove("separate_generic_port_alignment")
