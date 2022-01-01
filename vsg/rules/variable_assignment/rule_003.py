
from vsg import token

from vsg.rules import whitespace_before_token

lTokens = []
lTokens.append(token.simple_variable_assignment.assignment)
lTokens.append(token.conditional_variable_assignment.assignment)
lTokens.append(token.selected_variable_assignment.assignment)


class rule_003(whitespace_before_token):
    '''
    This rule checks for at least a single space before the assignment.

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
        whitespace_before_token.__init__(self, 'variable_assignment', '003', lTokens)
        self.solution = 'Ensure at least a single space exists before the *:=* keyword.'
