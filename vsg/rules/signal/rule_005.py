
from vsg import token

from vsg.rules import single_space_after_token

lTokens = []
lTokens.append(token.signal_declaration.colon)


class rule_005(single_space_after_token):
    '''
    Checks for a single space after the :.
    '''
    def __init__(self):
        single_space_after_token.__init__(self, 'signal', '005', lTokens)
        self.solution = 'Ensure only a signal space after the colon.'
