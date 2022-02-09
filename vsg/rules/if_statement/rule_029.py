
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.if_statement.then_keyword)


class rule_029(token_case):
    '''
    This rule checks the **then** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       if (a = '1') THEN

    **Fix**

    .. code-block:: vhdl

       if (a = '1') then
    '''

    def __init__(self):
        token_case.__init__(self, 'if', '029', lTokens)
        self.groups.append('case::keyword')
