
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.entity_declaration.entity_simple_name)


class rule_012(token_case_with_prefix_suffix):
    '''
    This rule checks the case of the entity name in the **end entity** statement.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end entity FIFO;

    **Fix**

    .. code-block:: vhdl

       end entity fifo;
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'entity', '012', lTokens)
        self.groups.append('case::name')
