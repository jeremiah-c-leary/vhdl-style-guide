
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.component_declaration.is_keyword)


class rule_006(token_case):
    '''
    This rule checks the **is** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       component fifo IS

       component fifo Is

    **Fix**

    .. code-block:: vhdl

       component fifo is

       component fifo is
    '''

    def __init__(self):
        token_case.__init__(self, 'component', '006', lTokens)
        self.groups.append('case::keyword')
