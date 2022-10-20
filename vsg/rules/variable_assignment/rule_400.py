
from vsg.rules import multiline_conditional_alignment as Rule

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.conditional_variable_assignment.assignment, token.conditional_variable_assignment.semicolon])


class rule_400(Rule):
    '''
    This rule checks alignment of multiline conditional variable assignments.

    |configuring_conditional_multiline_indent_rules_link|

    **Violation**

    .. code-block:: vhdl

       wr_en := '0' when q_wr_en = '1' else
            '1';

       w_foo := I_FOO when ((I_BAR = '1') and
                (I_CRUFT = '1')) else
                '0';

    **Fix**

    .. code-block:: vhdl

       wr_en := '0' when q_wr_en = '1' else
                '1';

       w_foo := I_FOO when ((I_BAR = '1') and
                            (I_CRUFT = '1')) else
                '0';
    '''

    def __init__(self):
        Rule.__init__(self, 'variable_assignment', '400', lTokenPairs)
