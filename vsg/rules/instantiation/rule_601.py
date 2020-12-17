
from vsg import token

from vsg.rules import token_prefix

lTokens = []
lTokens.append(token.component_instantiation_statement.instantiation_label)


class rule_601(token_prefix):
    '''
    Constant rule 601 checks for prefixes in package identifiers.
    '''

    def __init__(self):
        token_prefix.__init__(self, 'instantiation', '601', lTokens)
        self.prefixes = ['inst_']
        self.solution = 'instantiation label'
