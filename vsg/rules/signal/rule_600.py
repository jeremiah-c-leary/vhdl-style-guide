
from vsg.rules import token_suffix

from vsg import token

lTokens = []
lTokens.append(token.signal_declaration.identifier)


class rule_600(token_suffix):
    '''
    Signal rule 600 checks for suffixes in signal identifiers.
    '''

    def __init__(self):
        token_suffix.__init__(self, 'signal', '600', lTokens)
        self.suffixes = ['_s']
        self.solution = 'Signal identifiers'
