
from vsg.rules import token_indent as Rule

from vsg import token

lTokens = []
lTokens.append(token.concurrent_selected_signal_assignment.with_keyword)
lTokens.append(token.selected_force_assignment.with_keyword)
lTokens.append(token.selected_variable_assignment.with_keyword)
lTokens.append(token.selected_waveform_assignment.with_keyword)


class rule_300(Rule):
    '''
    This rule checks the indent of the **with** keyword.

    **Violation**

    .. code-block:: vhdl

       wr_en <= '1';

           with mux_sel select addr <=
         "0000" when 0,
         "0001" when 1,
         "1111" when others;

    **Fix**

    .. code-block:: vhdl

       wr_en <= '1';

       with mux_sel select addr <=
         "0000" when 0,
         "0001" when 1,
         "1111" when others;
    '''

    def __init__(self):
        Rule.__init__(self, 'selected_assignment', '300', lTokens)
