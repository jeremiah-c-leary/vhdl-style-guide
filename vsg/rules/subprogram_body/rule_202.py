
from vsg.rules import blank_line_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.begin_keyword)

lAllowTokens = []
lAllowTokens.append(token.subprogram_body.is_keyword)


class rule_202(blank_line_above_line_starting_with_token):
    '''
    This rule checks for blank lines above the **begin** keyword.

    This rule allows the **is** keyword to occupy the blank line:

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
        blank_line_above_line_starting_with_token.__init__(self, 'subprogram_body', '202', lTokens, lAllowTokens)
