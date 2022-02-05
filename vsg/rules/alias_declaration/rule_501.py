
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.alias_declaration.is_keyword)


class rule_501(token_case):
    '''
    This rule checks the **is** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       alias alias_designator IS name;

    **Fix**

    .. code-block:: vhdl

       alias alias_designator is name;
    '''

    def __init__(self):
        token_case.__init__(self, 'alias_declaration', '501', lTokens)
        self.groups.append('case::keyword')
