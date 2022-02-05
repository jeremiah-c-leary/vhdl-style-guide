
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.entity_declaration.entity_keyword)


class rule_004(token_case):
    '''
    This rule checks the **entity** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       ENTITY fifo is

    **Fix**

    .. code-block:: vhdl

       entity fifo is
    '''

    def __init__(self):
        token_case.__init__(self, 'entity', '004', lTokens)
        self.groups.append('case::keyword')
