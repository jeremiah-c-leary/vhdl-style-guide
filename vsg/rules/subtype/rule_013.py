
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.subtype_declaration.is_keyword)


class rule_013(token_case):
    '''
    This rule checks the **is** keyword in subtype definitions has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       subtype interface IS othertype
       subtype interface Is othertype
       subtype interface is othertype

    **Fix**

    .. code-block:: vhdl

       subtype interface is othertype
       subtype interface is othertype
       subtype interface is othertype
    '''

    def __init__(self):
        token_case.__init__(self, 'subtype', '013', lTokens)
        self.groups.append('case::keyword')
