
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.block_statement.end_keyword)


class rule_504(token_case):
    '''
    This rule checks the **end** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       END block block_label;

    **Fix**

    .. code-block:: vhdl

       end block block_label;
    '''

    def __init__(self):
        token_case.__init__(self, 'block', '504', lTokens)
        self.groups.append('case::keyword')
