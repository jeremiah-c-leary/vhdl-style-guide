# -*- coding: utf-8 -*-

from vsg.rules import (
    align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token,
)
from vsg.token import use_clause as token


class rule_009(align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token):
    """
    This rule checks alignment of comments above library use statements.

    **Violation**

    .. code-block:: vhdl

        library ieee;
        -- Use standard logic library
          use ieee.std_logic_1164.all;

    **Fix**

    .. code-block:: vhdl

        library ieee;
          -- Use standard logic library
          use ieee.std_logic_1164.all;
    """

    def __init__(self):
        super().__init__(token.keyword, bIncrement=True)
        self.solution = "Align comment with *use* keyword."
        self.subphase = 2
        self.configuration_documentation_link = None
