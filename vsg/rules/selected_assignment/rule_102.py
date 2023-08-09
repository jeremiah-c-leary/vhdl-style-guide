
from vsg.rules.whitespace_after_token import Rule

from vsg import token

lTokens = []
lTokens.append(token.concurrent_selected_signal_assignment.select_keyword)
lTokens.append(token.selected_force_assignment.select_keyword)
lTokens.append(token.selected_variable_assignment.select_keyword)
lTokens.append(token.selected_waveform_assignment.select_keyword)


class rule_102(Rule):
    '''
    This rule checks for a single space after the **select** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       with mux_sel select    addr <=
         "0000" when 0,
         "0001" when 1,
         "1111" when others;

    **Fix**

    .. code-block:: vhdl

       with mux_sel select addr <=
         "0000" when 0,
         "0001" when 1,
         "1111" when others;
    '''

    def __init__(self):
        Rule.__init__(self, 'selected_assignment', '102', lTokens)
