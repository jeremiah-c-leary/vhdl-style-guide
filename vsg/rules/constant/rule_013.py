
from vsg.rules import consistent_token_case

from vsg import token


class rule_013(consistent_token_case):
    '''
    Constant rule 013 checks case consistency of constant names.
    '''

    def __init__(self):
        consistent_token_case.__init__(self, 'constant', '013', [token.constant_declaration.identifier])
