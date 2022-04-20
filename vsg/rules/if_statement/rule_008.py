
from vsg.rules import remove_excessive_blank_lines_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.if_statement.end_keyword)

lOverrides = []
lOverrides.append(token.case_statement.semicolon)
lOverrides.append(token.loop_statement.semicolon)


class rule_008(remove_excessive_blank_lines_above_line_starting_with_token):
    '''
    This rule checks for blank lines before the **end if** keywords.

    **Violation**

    .. code-block:: vhdl

        e <= '0';


      end if;

    **Fix**

    .. code-block:: vhdl

        e <= '0';
      end if;
    '''
    def __init__(self):
        remove_excessive_blank_lines_above_line_starting_with_token.__init__(self, 'if', '008', lTokens, iAllow=0, lOverrides=lOverrides)
        self.solution = 'Remove blank line(s) before the *end if* keyword.'
