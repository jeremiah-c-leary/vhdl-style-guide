# -*- coding: utf-8 -*-

from vsg.rules import blank_line_above_line_starting_with_token
from vsg.token import context_declaration as token


class rule_024(blank_line_above_line_starting_with_token):
    """
    This rule checks for blank lines or comments above the **end** keyword.

    |configuring_blank_lines_link|

    The default style is :code:`no_code`.

    **Violation**

    .. code-block:: vhdl

         use ieee.std_logic_1164.all;
       end context;

    **Fix**

    .. code-block:: vhdl

         use ieee.std_logic_1164.all;

       end context;
    """

    def __init__(self):
        super().__init__([token.end_keyword])
