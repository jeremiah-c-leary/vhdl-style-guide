
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.semicolon)


class rule_205(blank_line_below_line_ending_with_token):
    '''
    This rule checks for a blank line below the end of the function declaration.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       function overflow (a: integer) return integer is
       end;
       signal wr_en : std_logic;

    **Fix**

    .. code-block:: vhdl

       function overflow (a: integer) return integer is
       end;

       signal wr_en : std_logic;
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'subprogram_body', '205', lTokens)
