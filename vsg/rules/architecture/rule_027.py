# -*- coding: utf-8 -*-

from vsg import parser, token
from vsg.rules import (
    align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens,
)

lAlign = []
lAlign.append(parser.comment)

lSkip = []
lSkip.append(parser.comment)


class rule_027(align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens):
    """
    This rule checks the alignment of inline comments in the architecture declarative part.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       architecture rtl of my_entity is

         signal   wr_en    : std_logic;  -- Comment 1
         signal   rd_en    : std_logic;     -- Comment 2
         constant c_period : time; -- Comment 3

       begin

    **Fix**

    .. code-block:: vhdl

       architecture rtl of my_entity is

         signal   wr_en    : std_logic; -- Comment 1
         signal   rd_en    : std_logic; -- Comment 2
         constant c_period : time;      -- Comment 3

       begin
    """

    def __init__(self):
        super().__init__(lAlign, token.architecture_body.is_keyword, token.architecture_body.begin_keyword, lSkip)
        self.solution = "Align comments."
        self.subphase = 5
