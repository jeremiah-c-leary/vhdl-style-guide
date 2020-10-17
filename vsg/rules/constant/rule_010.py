
from vsg import token

from vsg.rules import whitespace_before_token

lTokens = []
lTokens.append(token.constant_declaration.assignment_operator)


class rule_010(whitespace_before_token):
    '''
    Constant rule 010 checks for at least a single space before the := keyword.
    '''
    def __init__(self):
        whitespace_before_token.__init__(self, 'constant', '010', lTokens)
        self.solution = 'Ensure at least one space before :=.'
