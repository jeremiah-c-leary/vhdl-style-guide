
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.block_statement.is_keyword)


class rule_502(token_case):
    '''
    This rule checks the **is** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       block_label : block IS

    **Fix**

    .. code-block:: vhdl

       block_label : block is
    '''

    def __init__(self):
        token_case.__init__(self, 'block', '502', lTokens)
        self.groups.append('case::keyword')
