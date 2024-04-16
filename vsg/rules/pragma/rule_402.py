# -*- coding: utf-8 -*-

from vsg.rules import previous_line as Rule
from vsg.token import pragma as token


class rule_402(Rule):
    """
    This rule checks for blank lines or comments above closing pragmas.

    |configuring_previous_line_rules_link|

    |configuring_pragmas_link|

    The default style is :code:`no_blank_line`.

    **Violation**

    .. code-block:: vhdl

       end component;

       -- synthesis translate_off

    **Fix**

    .. code-block:: vhdl

       end component;
       -- synthesis translate_off
    """

    def __init__(self):
        super().__init__([token.close])
        self.style = "no_blank_line"
