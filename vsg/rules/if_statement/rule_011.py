
from vsg.rules import remove_excessive_blank_lines_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.if_statement.else_keyword)

lOverrides = []
lOverrides.append(token.case_statement.case_label)
lOverrides.append(token.case_statement.case_keyword)
lOverrides.append(token.loop_statement.loop_label)
lOverrides.append(token.loop_statement.loop_keyword)
lOverrides.append(token.iteration_scheme.while_keyword)
lOverrides.append(token.iteration_scheme.for_keyword)


class rule_011(remove_excessive_blank_lines_below_line_ending_with_token):
    '''
    This rule checks for blank lines after the **else** keyword.

    **Violation**

    .. code-block:: vhdl

      else


        e <= '0';

    **Fix**

    .. code-block:: vhdl

      else
        e <= '0';
    '''
    def __init__(self):
        remove_excessive_blank_lines_below_line_ending_with_token.__init__(self, 'if', '011', lTokens, iAllow=0, lOverrides=lOverrides)
        self.solution = 'Remove blank line(s) after the *else* keyword.'
