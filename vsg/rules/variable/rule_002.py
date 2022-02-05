
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.variable_declaration.variable_keyword)


class rule_002(token_case):
    '''
    This rule checks the **variable** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       VARIABLE count : integer;

    **Fix**

    .. code-block:: vhdl

       variable count : integer;
    '''

    def __init__(self):
        token_case.__init__(self, 'variable', '002', lTokens)
        self.groups.append('case::keyword')
