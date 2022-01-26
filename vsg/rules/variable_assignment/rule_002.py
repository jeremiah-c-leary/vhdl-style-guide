
from vsg import parser
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.simple_variable_assignment.assignment, parser.todo])
lTokens.append([token.conditional_variable_assignment.assignment, parser.todo])
lTokens.append([token.selected_variable_assignment.assignment, parser.todo])


class rule_002(single_space_between_token_pairs):
    '''
    This rule checks for a single space after the assignment.

    **Violation**

    .. code-block:: vhdl

         counter :=0;
         count   :=     counter + 1;

    **Fix**

    .. code-block:: vhdl

         counter := 0;
         count   := counter + 1;
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'variable_assignment', '002', lTokens)
        self.solution = 'Ensure a single space after the :=.'
