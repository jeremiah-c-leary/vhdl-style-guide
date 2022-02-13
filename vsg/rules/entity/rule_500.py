
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.entity_declaration.begin_keyword)


class rule_500(token_case):
    '''
    This rule checks the **begin** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       entity fifo is

       BEGIN

       end entity;

    **Fix**

    .. code-block:: vhdl

       entity fifo is

       begin

       end entity;
    '''

    def __init__(self):
        token_case.__init__(self, 'entity', '500', lTokens)
        self.groups.append('case::keyword')
