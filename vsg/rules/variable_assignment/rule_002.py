
from vsg import parser
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.simple_variable_assignment.assignment, parser.todo])
lTokens.append([token.conditional_variable_assignment.assignment, parser.todo])
lTokens.append([token.selected_variable_assignment.assignment, parser.todo])


class rule_002(single_space_between_token_pairs):
    '''
    Checks for a single space after the :=.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'variable_assignment', '002', lTokens)
        self.solution = 'Ensure a single space after the :=.'
