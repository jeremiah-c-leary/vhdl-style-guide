
from vsg.rules.whitespace_between_token_pairs import Rule

from vsg import token

lTokens = []
lTokens.append([token.concurrent_simple_signal_assignment.target, token.concurrent_simple_signal_assignment.assignment])
lTokens.append([token.concurrent_conditional_signal_assignment.target, token.concurrent_conditional_signal_assignment.assignment])
lTokens.append([token.concurrent_selected_signal_assignment.target, token.concurrent_selected_signal_assignment.assignment])


class rule_004(Rule):
    '''
    This rule checks for at least a single space before the **<=** operator.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       wr_en<= '0';

    **Fix**

    .. code-block:: vhdl

       wr_en <= '0';
    '''
    def __init__(self):
        Rule.__init__(self, 'concurrent', '004', lTokens)
        self.number_of_spaces = '>=1'
