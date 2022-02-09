
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.block_statement.block_keyword)


class rule_501(token_case):
    '''
    This rule checks the **block** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       block_label : BLOCK is

    **Fix**

    .. code-block:: vhdl

       block_label : block is
    '''

    def __init__(self):
        token_case.__init__(self, 'block', '501', lTokens)
        self.groups.append('case::keyword')
