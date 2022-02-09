
from vsg.rules import blank_line_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.block_statement.begin_keyword)

lAllowTokens = []
lAllowTokens.append(token.block_statement.is_keyword)
lAllowTokens.append(token.block_statement.guard_close_parenthesis)


class rule_202(blank_line_above_line_starting_with_token):
    '''
    This rule checks for blank lines or comments above the **begin** keyword.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       block_label block is

         constant width : integer := 32;
       begin

    **Fix**

    .. code-block:: vhdl

       block_label block is

         constant width : integer := 32;

       begin
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'block', '202', lTokens, lAllowTokens)
