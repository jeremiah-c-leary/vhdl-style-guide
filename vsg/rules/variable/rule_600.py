
from vsg.rules import token_suffix

from vsg import token

lTokens = []
lTokens.append(token.variable_declaration.identifier)


class rule_600(token_suffix):
    '''
    Variable rule 600 checks for suffixes in variable identifiers.
    '''

    def __init__(self):
        token_suffix.__init__(self, 'variable', '600', lTokens)
        self.suffixes = ['_v']
        self.solution = 'Variable identifiers'
