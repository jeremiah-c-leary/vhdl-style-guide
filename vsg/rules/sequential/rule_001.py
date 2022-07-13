
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.signal_assignment_statement.label)
lTokens.append(token.simple_force_assignment.target)
lTokens.append(token.simple_waveform_assignment.target)
lTokens.append(token.conditional_waveform_assignment.target)


class rule_001(token_indent):
    '''
    This rule checks the indent of sequential statements.

    **Violation**

    .. code-block:: vhdl

       begin

           wr_en <= '1';
       rd_en <= '0';

    **Fix**

    .. code-block:: vhdl

       begin

         wr_en <= '1';
         rd_en <= '0';
    '''

    def __init__(self):
        token_indent.__init__(self, 'sequential', '001', lTokens)
