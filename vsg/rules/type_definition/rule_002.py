
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.incomplete_type_declaration.type_keyword)
lTokens.append(token.full_type_declaration.type_keyword)


class rule_002(token_case):
    '''
    This rule checks the **type** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       TYPE state_machine is (idle, write, read, done);

    **Fix**

    .. code-block:: vhdl

       type state_machine is (idle, write, read, done);
    '''

    def __init__(self):
        token_case.__init__(self, 'type', '002', lTokens)
        self.groups.append('case::keyword')
