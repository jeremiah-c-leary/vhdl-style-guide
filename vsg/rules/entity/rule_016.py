# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import blank_line_above_line_starting_with_token

lTokens = []
lTokens.append(token.entity_declaration.end_keyword)


class rule_016(blank_line_above_line_starting_with_token):
    """
    This rule checks for blank lines above the **end entity** keywords.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

           wr_en : in    std_logic;
           rd_en : in    std_logic
         );


       end entity fifo;


    **Fix**

    .. code-block:: vhdl

           wr_en : in    std_logic;
           rd_en : in    std_logic
         );
       end entity fifo;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.style = "no_blank_line"
