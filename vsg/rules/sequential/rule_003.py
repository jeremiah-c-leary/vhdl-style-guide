
from vsg import token

from vsg.rules import whitespace_before_token

lTokens = []
lTokens.append(token.simple_force_assignment.assignment)
lTokens.append(token.simple_waveform_assignment.assignment)
lTokens.append(token.simple_release_assignment.assignment)


class rule_003(whitespace_before_token):
    '''
    This rule checks for at least a single space before the **<=** operator.

    **Violation**

    .. code-block:: vhdl

       wr_en<= '1';
       rd_en   <= '0';

    **Fix**

    .. code-block:: vhdl

       wr_en <= '1';
       rd_en   <= '0';
    '''
    def __init__(self):
        whitespace_before_token.__init__(self, 'sequential', '003', lTokens)
        self.solution = 'Ensure at least a single space exists before the *<=* keyword.'
