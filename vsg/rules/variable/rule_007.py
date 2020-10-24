
from vsg.rules import existence_of_tokens_which_should_not_occur

from vsg import token

lTokens = []
lTokens.append(token.variable_declaration.assignment_operator)


class rule_007(existence_of_tokens_which_should_not_occur):
    '''
    Checks for default assignments in variable declarations.
    '''

    def __init__(self):
        existence_of_tokens_which_should_not_occur.__init__(self, 'variable', '007', lTokens)
        self.solution = 'Remove default assignment.'
