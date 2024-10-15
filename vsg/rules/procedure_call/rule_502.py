# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_in_range_bounded_by_tokens

lTokens = []
lTokens.append(token.association_element.formal_part)


class rule_502(token_case_in_range_bounded_by_tokens):
    """
    This rule checks the port names have proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       port (
         wr_en     : in    std_logic;
         rd_en     : in    std_logic;
         OVERFLOW  : out   std_logic;
         underflow : out   std_logic
       );

    **Fix**

    .. code-block:: vhdl

       port (
         wr_en     : in    std_logic;
         rd_en     : in    std_logic;
         overflow  : out   std_logic;
         underflow : out   std_logic
       );
    """

    def __init__(self):
        super().__init__(lTokens, token.procedure_call.open_parenthesis, token.procedure_call.close_parenthesis)
        self.configuration.append("prefix_exceptions")
        self.configuration.append("suffix_exceptions")
        self.configuration.append("case_exceptions")
        self.groups.append("case::name")
