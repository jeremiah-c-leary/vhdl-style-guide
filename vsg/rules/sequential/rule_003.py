
from vsg import token

from vsg.rules.whitespace_before_token import Rule

lTokens = []
lTokens.append(token.simple_force_assignment.assignment)
lTokens.append(token.simple_waveform_assignment.assignment)
lTokens.append(token.simple_release_assignment.assignment)


class rule_003(Rule):
    '''
    This rule checks for at least a single space before the **<=** operator.

    |configuring_whitespace_rules_link|

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
        Rule.__init__(self, 'sequential', '003', lTokens)
        self.number_of_spaces = '>=1'
