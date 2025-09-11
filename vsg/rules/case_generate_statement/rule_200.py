# -*- coding: utf-8 -*-

from vsg.rules import blank_line_above_line_starting_with_token
from vsg.token import case_generate_statement as token


class rule_200(blank_line_above_line_starting_with_token):
    """
    This rule checks for blank lines or comments above the **end** keyword.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

         when others =>
           null;
       end generate;

    **Fix**

    .. code-block:: vhdl

         when others =>
           null;

       end generate;
    """

    def __init__(self):
        super().__init__([token.end_keyword])
