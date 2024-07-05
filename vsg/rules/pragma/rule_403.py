# -*- coding: utf-8 -*-

from vsg.rules import blank_line_below_line_ending_with_token as Rule
from vsg.token import pragma as token


class rule_403(Rule):
    """
    This rule checks for a blank line below closing pragmas.

    |configuring_blank_lines_link|

    |configuring_pragmas_link|

    The default style is :code:`require_blank_line`.

    **Violation**

    .. code-block:: vhdl

       -- synthesis translate_off
       signal rd_en : std_logic;


    **Fix**

    .. code-block:: vhdl

       -- synthesis translate_off

       signal rd_en : std_logic;
    """

    def __init__(self):
        super().__init__([token.close])
        self.style = "require_blank_line"
