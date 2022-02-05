
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.entity_declaration.is_keyword)


class rule_006(token_case):
    '''
    This rule checks the **is** keyword has proper case in the entity declaration.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       entity fifo IS

    **Fix**

    .. code-block:: vhdl

       entity fifo is
    '''

    def __init__(self):
        token_case.__init__(self, 'entity', '006', lTokens)
        self.groups.append('case::keyword')
