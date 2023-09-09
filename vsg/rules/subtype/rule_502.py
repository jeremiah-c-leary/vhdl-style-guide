
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.subtype_declaration.is_keyword)


class rule_502(token_case):
    '''
    This rule checks the **is** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       subtype interface IS record
       subtype interface Is record
       subtype interface is record

    **Fix**

    .. code-block:: vhdl

       subtype interface is record
       subtype interface is record
       subtype interface is record
    '''

    def __init__(self):
        token_case.__init__(self, 'subtype', '502', lTokens)
        self.groups.append('case::keyword')
