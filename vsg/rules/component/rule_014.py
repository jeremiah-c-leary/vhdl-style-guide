
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.component_declaration.end_component_keyword)


class rule_014(token_case):
    '''
    This rule checks the **component** keyword in the **end component** line has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end COMPONENT fifo;

    **Fix**

    .. code-block:: vhdl

       end component fifo;
    '''

    def __init__(self):
        token_case.__init__(self, 'component', '014', lTokens)
        self.groups.append('case::keyword')
