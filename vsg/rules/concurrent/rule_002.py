
from vsg.rules import single_space_after_token

from vsg import token

lTokens = []
lTokens.append(token.concurrent_simple_signal_assignment.assignment)
lTokens.append(token.concurrent_conditional_signal_assignment.assignment)
lTokens.append(token.concurrent_selected_signal_assignment.assignment)


class rule_002(single_space_after_token):
    '''
    This rule checks for a single space after the **<=** operator.

    **Violation**

    .. code-block:: vhdl

       wr_en <=    '0';
       rd_en <=   '1';

    **Fix**

    .. code-block:: vhdl

       wr_en <= '0';
       rd_en <= '1';
    '''

    def __init__(self):
        single_space_after_token.__init__(self, 'concurrent', '002', lTokens)
