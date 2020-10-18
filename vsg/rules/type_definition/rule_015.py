
from vsg.rules import token_prefix

from vsg import token

lTokens = []
lTokens.append(token.incomplete_type_declaration.identifier)
lTokens.append(token.full_type_declaration.identifier)


class rule_015(token_prefix):
    '''
    Checks for prefixes in type identifiers.
    '''

    def __init__(self):
        token_prefix.__init__(self, 'type', '015', lTokens)
        self.prefixes = ['t_']
        self.solution = 'Type identifiers'
