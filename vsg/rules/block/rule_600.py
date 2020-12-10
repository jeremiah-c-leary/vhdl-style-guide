
from vsg import token

from vsg.rules import token_suffix

lTokens = []
lTokens.append(token.block_statement.block_label)
lTokens.append(token.block_statement.end_block_label)


class rule_600(token_suffix):
    '''
    Constant rule 600 checks for suffixes in block labels.
    '''

    def __init__(self):
        token_suffix.__init__(self, 'block', '600', lTokens)
        self.suffixes = ['_blk']
