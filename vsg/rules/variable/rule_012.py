
from vsg.rules import token_prefix

from vsg import token

lTokens = []
lTokens.append(token.variable_declaration.identifier)


class rule_012(token_prefix):
    '''
    Variable rule 012 checks for prefixes in variable identifiers.
    '''

    def __init__(self):
        token_prefix.__init__(self, 'variable', '012', lTokens)
        self.prefixes = ['v_']
        self.solution = 'Variable identifiers'
