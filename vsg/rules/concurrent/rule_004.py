
from vsg.rules import single_space_between_token_pairs

from vsg import token

lTokens = []
lTokens.append([token.concurrent_simple_signal_assignment.target, token.concurrent_simple_signal_assignment.assignment])
lTokens.append([token.concurrent_conditional_signal_assignment.target, token.concurrent_conditional_signal_assignment.assignment])
lTokens.append([token.concurrent_selected_signal_assignment.target, token.concurrent_selected_signal_assignment.assignment])


class rule_004(single_space_between_token_pairs):
    '''
    This rule checks for at least a single space before the **<=** operator.

    **Violation**

    .. code-block:: vhdl

       wr_en<= '0';

    **Fix**

    .. code-block:: vhdl

       wr_en <= '0';
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'concurrent', '004', lTokens, bMinimum=True)
        self.solution = 'Ensure a single space between target and assignment.'
