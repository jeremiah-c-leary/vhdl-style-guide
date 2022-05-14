
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.block_statement.end_keyword, token.block_statement.end_block_keyword])
lTokens.append([token.block_statement.end_block_keyword, token.block_statement.end_block_label])


class rule_101(Rule):
    '''
    This rule checks for a single space between the **end** and **block** keywords and label.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       end   block   block_label;

    **Fix**

    .. code-block:: vhdl

       end block block_label;
    '''
    def __init__(self):
        Rule.__init__(self, 'block', '101', lTokens)
