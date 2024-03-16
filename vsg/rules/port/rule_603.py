# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_prefix as Rule, utils

lTokens = []


class rule_603(Rule):
    """
    This rule checks for valid prefixes on port identifiers for buffer ports.

    The default prefix is: *b_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       port (
         wr_en    : buffer    std_logic;
         rd_en    : buffer    std_logic
       );


    **Fix**

    .. code-block:: vhdl

       port (
         b_wr_en    : buffer    std_logic;
         b_rd_en    : buffer    std_logic
       );
    """

    def __init__(self):
        super().__init__(lTokens)
        self.prefixes = ["b_"]

    def _get_tokens_of_interest(self, oFile):
        lReturn = []
        lToi = oFile.get_interface_elements_between_tokens(token.port_clause.open_parenthesis, token.port_clause.close_parenthesis)
        lReturn = utils.extract_identifiers_with_mode_of_buffer(lToi)
        return lReturn
