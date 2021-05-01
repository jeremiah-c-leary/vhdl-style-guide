
from vsg import token

from vsg.rules import token_suffix

lTokens = []
lTokens.append(token.subtype_declaration.identifier)


class rule_600(token_suffix):
    '''
    Subtype rule 600 checks for suffixes in user defined subtype identifiers.
    '''

    def __init__(self):
        token_suffix.__init__(self, 'subtype', '600', lTokens)
        self.suffixes = ['_st']
