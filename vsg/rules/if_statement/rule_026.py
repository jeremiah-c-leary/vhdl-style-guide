
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.if_statement.elsif_keyword)


class rule_026(token_case):
    '''
    This rule checks the **elsif** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       ELSIF (a = '1') then

    **Fix**

    .. code-block:: vhdl

       elsif (a = '1') then
    '''

    def __init__(self):
        token_case.__init__(self, 'if', '026', lTokens)
        self.groups.append('case::keyword')
