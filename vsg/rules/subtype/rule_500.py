
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.subtype_declaration.subtype_keyword)


class rule_500(token_case):
    '''
    This rule checks the **subtype** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       SUBTYPE interface is record
       Subtype interface is record
       subtype interface is record

    **Fix**

    .. code-block:: vhdl

       subtype interface is record
       subtype interface is record
       subtype interface is record
    '''

    def __init__(self):
        token_case.__init__(self, 'subtype', '500', lTokens)
        self.groups.append('case::keyword')
