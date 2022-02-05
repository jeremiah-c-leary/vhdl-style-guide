
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.constant_declaration.constant_keyword)


class rule_002(token_case):
    '''
    This rule checks the **constant** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       CONSTANT size : integer := 1;

    **Fix**

    .. code-block:: vhdl

       constant size : integer := 1;
    '''

    def __init__(self):
        token_case.__init__(self, 'constant', '002', lTokens)
        self.groups.append('case::keyword')
