
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.full_type_declaration.is_keyword)


class rule_013(token_case):
    '''
    This rule checks the **is** keyword in type definitions has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       type interface IS record
       type interface Is record
       type interface is record

    **Fix**

    .. code-block:: vhdl

       type interface is record
       type interface is record
       type interface is record
    '''

    def __init__(self):
        token_case.__init__(self, 'type', '013', lTokens)
        self.groups.append('case::keyword')
