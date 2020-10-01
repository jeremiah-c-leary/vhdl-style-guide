
from vsg import parser

from vsg.rules import whitespace_before_token

from vsg import token


class rule_006(whitespace_before_token):
    '''
    Constant rule 006 checks there is at least a single space before the colon.
    '''
    def __init__(self):
        whitespace_before_token.__init__(self, 'constant', '006', token.constant_declaration.colon)
        self.solution = 'Ensure at least one space before colon.'
