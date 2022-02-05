
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.case_statement.is_keyword)


class rule_015(token_case):
    '''
    This rule checks the **is** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

         case address IS

         case address Is

         case address iS

    **Fix**

    .. code-block:: vhdl

         case address is

         case address is

         case address is
    '''

    def __init__(self):
        token_case.__init__(self, 'case', '015', lTokens)
        self.groups.append('case::keyword')
