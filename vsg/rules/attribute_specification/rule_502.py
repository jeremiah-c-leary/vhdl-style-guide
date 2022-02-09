
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.attribute_specification.of_keyword)


class rule_502(token_case):
    '''
    This rule checks the **of** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       attribute coordinate OF comp_1 : component is (0.0, 17.5);

    **Fix**

    .. code-block:: vhdl

       attribute coordinate of comp_1 : component is (0.0, 17.5);
    '''

    def __init__(self):
        token_case.__init__(self, 'attribute_specification', '502', lTokens)
        self.groups.append('case::keyword')
