
from vsg import token

from vsg.rules.whitespace_before_token import Rule

lTokens = []
lTokens.append(token.simple_variable_assignment.assignment)
lTokens.append(token.conditional_variable_assignment.assignment)
lTokens.append(token.selected_variable_assignment.assignment)


class rule_003(Rule):
    '''
    This rule checks for at least a single space before the assignment.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

         counter:= 0;
         count := counter + 1;

    **Fix**

    .. code-block:: vhdl

         counter := 0;
         count := counter + 1;
    '''
    def __init__(self):
        Rule.__init__(self, 'variable_assignment', '003', lTokens)
        self.number_of_spaces = '>=1'
