
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.case_statement.case_keyword)


class rule_014(token_case):
    '''
    This rule checks the **case** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

         CASE address is

         Case address is

         case address is

    **Fix**

    .. code-block:: vhdl

         case address is

         case address is

         case address is
    '''

    def __init__(self):
        token_case.__init__(self, 'case', '014', lTokens)
        self.groups.append('case::keyword')
