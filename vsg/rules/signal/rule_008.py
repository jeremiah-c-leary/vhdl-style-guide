
from vsg.rules import token_prefix

from vsg import token

lTokens = []
lTokens.append(token.signal_declaration.identifier)


class rule_008(token_prefix):
    '''
    Signal rule 008 checks for prefixes in signal identifiers.
    '''

    def __init__(self):
        token_prefix.__init__(self, 'signal', '008', lTokens)
        self.prefixes = ['s_']
        self.solution = 'Signal identifiers'
