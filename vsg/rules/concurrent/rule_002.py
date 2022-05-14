
from vsg.rules.whitespace_after_token import Rule

from vsg import token

lTokens = []
lTokens.append(token.concurrent_simple_signal_assignment.assignment)
lTokens.append(token.concurrent_conditional_signal_assignment.assignment)
lTokens.append(token.concurrent_selected_signal_assignment.assignment)


class rule_002(Rule):
    '''
    This rule checks for a single space after the **<=** operator.

    |configuring_whitespace_rules_link|

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
        Rule.__init__(self, 'concurrent', '002', lTokens)
