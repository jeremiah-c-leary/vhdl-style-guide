
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.block_statement.begin_keyword)


class rule_503(token_case):
    '''
    This rule checks the **begin** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       block_label : block is
       BEGIN

    **Fix**

    .. code-block:: vhdl

       block_label : block is
       begin
    '''

    def __init__(self):
        token_case.__init__(self, 'block', '503', lTokens)
        self.groups.append('case::keyword')
