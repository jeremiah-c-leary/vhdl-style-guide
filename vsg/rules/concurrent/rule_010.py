
from vsg.rules import blank_lines_between_token_pairs

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.concurrent_simple_signal_assignment.target, token.concurrent_simple_signal_assignment.semicolon])
lTokenPairs.append([token.concurrent_conditional_signal_assignment.target, token.concurrent_conditional_signal_assignment.semicolon])
lTokenPairs.append([token.concurrent_selected_signal_assignment.with_keyword, token.concurrent_selected_signal_assignment.semicolon])


class rule_010(blank_lines_between_token_pairs):
    '''
    This rule removes blank lines within concurrent signal assignments.

    **Violation**

    .. code-block:: vhdl

       wr_en <= '0' when q_wr_en = '1' else

            '1';

       w_foo <= I_FOO when ((I_BAR = '1') and

                            (I_CRUFT = '1')) else

                '0';

    **Fix**

    .. code-block:: vhdl

       wr_en <= '0' when q_wr_en = '1' else
                '1';

       w_foo <= I_FOO when ((I_BAR = '1') and
                            (I_CRUFT = '1')) else
                '0';
    '''

    def __init__(self):
        blank_lines_between_token_pairs.__init__(self, 'concurrent', '010', lTokenPairs)
