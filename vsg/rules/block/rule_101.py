
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.block_statement.end_keyword, token.block_statement.end_block_keyword])
lTokens.append([token.block_statement.end_block_keyword, token.block_statement.end_block_label])


class rule_101(single_space_between_token_pairs):
    '''
    This rule checks for a single space between the **end** and **block** keywords and label.

    **Violation**

    .. code-block:: vhdl

       end   block   block_label;

    **Fix**

    .. code-block:: vhdl

       end block block_label;
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'block', '101', lTokens)
