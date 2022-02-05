
from vsg.rules import blank_line_below_line_ending_with_token

from vsg.token import case_statement_alternative as token

lTokens = []
lTokens.append(token.assignment)


class rule_200(blank_line_below_line_ending_with_token):
    '''
    This rule checks for a blank line below the **=>** keyword.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       when 0 =>
         a <= b;

    **Fix**

    .. code-block:: vhdl

       when 0 =>

         a <= b;
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'case', '200', lTokens)
