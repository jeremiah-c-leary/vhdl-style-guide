
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.context_declaration.is_keyword)


class rule_013(token_case):
    '''
    This rule checks the **is** keyword has proper case in the context declaration.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       context c1 IS

    **Fix**

    .. code-block:: vhdl

       context c1 is
    '''

    def __init__(self):
        token_case.__init__(self, 'context', '013', lTokens)
        self.groups.append('case::keyword')
