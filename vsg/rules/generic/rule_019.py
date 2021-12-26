
from vsg.rules import remove_excessive_blank_lines_above_line_starting_with_token

from vsg.token import generic_clause as token

lTokens = []
lTokens.append(token.close_parenthesis)


class rule_019(remove_excessive_blank_lines_above_line_starting_with_token):
    '''
    This rule checks for blank lines before the ); of the generic declaration.

    **Violation**

    .. code-block:: vhdl

      generic (
        g_width : std_logic := '0';
        g_depth : Std_logic := '1'


      );

    **Fix**

    .. code-block:: vhdl

      generic (
        g_width : std_logic := '0';
        g_depth : Std_logic := '1'
      );
    '''
    def __init__(self):
        remove_excessive_blank_lines_above_line_starting_with_token.__init__(self, 'generic', '019', lTokens, iAllow=0)
