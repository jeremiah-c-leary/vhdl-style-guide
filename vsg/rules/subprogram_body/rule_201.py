
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.is_keyword)

lAllowTokens = []
lAllowTokens.append(token.subprogram_body.begin_keyword)


class rule_201(blank_line_below_line_ending_with_token):
    '''
    This rule checks for a blank line below the **is** keyword.

    This rule allows the **begin** keyword to occupy the blank line:

    .. code-block:: vhdl

       function overflow (a: integer) return integer is
       begin

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       function overflow (a: integer) return integer is
         constant width : integer := 32;
       begin

    **Fix**

    .. code-block:: vhdl

       function overflow (a: integer) return integer is

         constant width : integer := 32;
       begin
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'subprogram_body', '201', lTokens, lAllowTokens)
