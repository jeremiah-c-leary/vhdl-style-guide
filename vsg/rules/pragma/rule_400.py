# -*- coding: utf-8 -*-

from vsg.rules import previous_line as Rule
from vsg.token import pragma as token


class rule_400(Rule):
    """
    This rule checks for blank lines or comments above opening pragmas.

    |configuring_previous_line_rules_link|

    |configuring_pragmas_link|

    The default style is :code:`no_code`.

    **Violation**

    .. code-block:: vhdl

       end component;
       -- synthesis translate_on

    **Fix**

    .. code-block:: vhdl

       end component;

       -- synthesis translate_on
    """

    def __init__(self):
        super().__init__([token.open])
        self.style = "no_code"
