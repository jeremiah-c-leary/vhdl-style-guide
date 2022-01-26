
from vsg.rules import remove_excessive_blank_lines_below_line_ending_with_token

from vsg.token import context_declaration as token


class rule_026(remove_excessive_blank_lines_below_line_ending_with_token):
    '''
    This rule ensures a single blank line after the **context** keword.

    **Violation**

    .. code-block:: vhdl

       context c1 is



         library ieee;

    **Fix**

    .. code-block:: vhdl

       context c1 is

         library ieee;
    '''
    def __init__(self):
        remove_excessive_blank_lines_below_line_ending_with_token.__init__(self, 'context', '026', [token.is_keyword])
