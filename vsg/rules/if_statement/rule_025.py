
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.if_statement.if_keyword)


class rule_025(token_case):
    '''
    This rule checks the **if** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       IF (a = '1') then

    **Fix**

    .. code-block:: vhdl

       if (a = '1') then
    '''

    def __init__(self):
        token_case.__init__(self, 'if', '025', lTokens)
        self.groups.append('case::keyword')
