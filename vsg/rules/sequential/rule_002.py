
from vsg import token

from vsg.rules.whitespace_after_token import Rule

lTokens = []
lTokens.append(token.simple_waveform_assignment.assignment)
lTokens.append(token.simple_force_assignment.assignment)
lTokens.append(token.simple_release_assignment.assignment)
lTokens.append(token.selected_waveform_assignment.assignment)
lTokens.append(token.selected_force_assignment.assignment)
lTokens.append(token.conditional_waveform_assignment.assignment)
lTokens.append(token.conditional_force_assignment.assignment)


class rule_002(Rule):
    '''
    This rule checks for a single space after the **<=** operator.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       wr_en <=     '1';
       rd_en <='0';

    **Fix**

    .. code-block:: vhdl

       wr_en <= '1';
       rd_en <= '0';
    '''
    def __init__(self):
        Rule.__init__(self, 'sequential', '002', lTokens)
