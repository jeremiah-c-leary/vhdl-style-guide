
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.component_declaration.component_keyword)


class rule_004(token_case):
    '''
    This rule checks the **component** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       COMPONENT fifo is

       Component fifo is

    **Fix**

    .. code-block:: vhdl

       component fifo is

       component fifo is
    '''

    def __init__(self):
        token_case.__init__(self, 'component', '004', lTokens)
        self.groups.append('case::keyword')
