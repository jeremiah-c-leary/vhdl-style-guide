
from vsg.rules import token_suffix

from vsg import token

lTokens = []
lTokens.append(token.incomplete_type_declaration.identifier)
lTokens.append(token.full_type_declaration.identifier)


class rule_600(token_suffix):
    '''
    Checks for suffixes in type identifiers.
    '''

    def __init__(self):
        token_suffix.__init__(self, 'type', '600', lTokens)
        self.suffixes = ['_t']
        self.solution = 'Type identifiers'
