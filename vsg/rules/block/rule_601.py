
from vsg import token

from vsg.rules import token_prefix

lTokens = []
lTokens.append(token.block_statement.block_label)
lTokens.append(token.block_statement.end_block_label)


class rule_601(token_prefix):
    '''
    Constant rule 601 checks for prefixes in package identifiers.
    '''

    def __init__(self):
        token_prefix.__init__(self, 'block', '601', lTokens)
        self.prefixes = ['blk_']
        self.solution = 'block label'
