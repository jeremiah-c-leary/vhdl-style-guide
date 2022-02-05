
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.begin_keyword)


class rule_203(blank_line_below_line_ending_with_token):
    '''
    This rule checks for a blank line below the **begin** keyword.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       function overflow (a: integer) return integer is
       begin
         a <= b;

    **Fix**

    .. code-block:: vhdl

       function overflow (a: integer) return integer is
       begin

         a <= b;
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'subprogram_body', '203', lTokens)
