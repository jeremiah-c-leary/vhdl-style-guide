
from vsg import parser

from vsg.rules import whitespace_before_token

from vsg import token


class rule_010(whitespace_before_token):
    '''
    Constant rule 010 checks for at least a single space before the := keyword.
    '''
    def __init__(self):
        whitespace_before_token.__init__(self, 'constant', '010', token.constant_declaration.assignment_operator)
        self.solution = 'Ensure at least one space before :=.'
