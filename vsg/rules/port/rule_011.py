# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_prefix_between_tokens_unless_between_tokens as Rule

lTokens = []
lTokens.append(token.interface_constant_declaration.identifier)
lTokens.append(token.interface_signal_declaration.identifier)
lTokens.append(token.interface_variable_declaration.identifier)
lTokens.append(token.interface_unknown_declaration.identifier)

oStart = token.port_clause.open_parenthesis
oEnd = token.port_clause.close_parenthesis

lUnless = []
lUnless.append([token.component_declaration.component_keyword, token.component_declaration.semicolon])


class rule_011(Rule):
    """
    This rule checks for valid prefixes on port identifiers.
    The default port prefixes are: *i_*, *o_*, *io_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       port (
         wr_en    : in    std_logic;
         rd_en    : in    std_logic;
         overflow : out   std_logic;
         data     : inout std_logic
       );


    **Fix**

    .. code-block:: vhdl

       port (
         i_wr_en    : in    std_logic;
         i_rd_en    : in    std_logic;
         o_overflow : out   std_logic;
         io_data    : inout std_logic
       );
    """

    def __init__(self):
        super().__init__(lTokens, oStart, oEnd, lUnless)
        self.prefixes = ["i_", "o_", "io_"]
