
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.block_statement.end_block_keyword)


class rule_505(token_case):
    '''
    This rule checks the **block** keyword in the **end block** has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end BLOCK block_label;

    **Fix**

    .. code-block:: vhdl

       end block block_label;
    '''

    def __init__(self):
        token_case.__init__(self, 'block', '505', lTokens)
        self.groups.append('case::keyword')
