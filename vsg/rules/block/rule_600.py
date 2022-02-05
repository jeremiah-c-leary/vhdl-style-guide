
from vsg import token

from vsg.rules import token_suffix

lTokens = []
lTokens.append(token.block_statement.block_label)
lTokens.append(token.block_statement.end_block_label)


class rule_600(token_suffix):
    '''
    This rule checks for valid suffixes on block labels.
    The default suffix is *_blk*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       block_label : block is

    **Fix**

    .. code-block:: vhdl

       block_label_blk : block is
    '''

    def __init__(self):
        token_suffix.__init__(self, 'block', '600', lTokens)
        self.suffixes = ['_blk']
