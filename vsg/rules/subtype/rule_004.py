
from vsg import token

from vsg.rules import token_prefix

lTokens = []
lTokens.append(token.subtype_declaration.identifier)


class rule_004(token_prefix):
    '''
    Subtype rule 004 checks for prefixes in user defined subtype identifiers.
    '''

    def __init__(self):
        token_prefix.__init__(self, 'subtype', '004', lTokens)
        self.prefixes = ['st_']
