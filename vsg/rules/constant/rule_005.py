
from vsg.rules import single_space_after_token

from vsg import token

lTokens = []
lTokens.append(token.constant_declaration.colon)


class rule_005(single_space_after_token):
    '''
    Constant rule 005 checks there is a single space after the colon.
    '''

    def __init__(self):
        single_space_after_token.__init__(self, 'constant', '005', lTokens)
