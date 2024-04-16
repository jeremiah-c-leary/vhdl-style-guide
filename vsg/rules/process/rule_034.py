# -*- coding: utf-8 -*-

from vsg import parser, token
from vsg.rules import (
    align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens,
)

lAlign = []
lAlign.append(parser.comment)

oStart = token.process_statement.process_keyword
oEnd = token.process_statement.begin_keyword

lSkip = []
lSkip.append(parser.comment)


class rule_034(align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens):
    """
    This rule aligns inline comments between the end of the process sensitivity list and the process **begin** keyword.
    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       proc_1 : process () is

          variable counter : integer range 0 to 31;     -- Counts the number of frames received
          variable width   : natural range 0 to 255; -- Keeps track of the data word size

          variable size    : natural range 0 to 7; -- Keeps track of the frame size

       begin

    **Fix**

    .. code-block:: vhdl

       proc_1 : process () is

          variable counter : integer range 0 to 31;  -- Counts the number of frames received
          variable width   : natural range 0 to 255; -- Keeps track of the data word size

          variable size    : natural range 0 to 7;   -- Keeps track of the frame size

       begin
    """

    def __init__(self):
        super().__init__(lAlign, oStart, oEnd, lSkip)
        self.solution = "Align comment."
        self.subphase = 4
        self.blank_line_ends_group = "no"
        self.comment_line_ends_group = "no"
