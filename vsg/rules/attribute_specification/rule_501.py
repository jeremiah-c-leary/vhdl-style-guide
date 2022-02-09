
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.attribute_specification.attribute_designator)


class rule_501(token_case_with_prefix_suffix):
    '''
    This rule checks the *attribute_designator* has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       attribute COORDINATE of comp_1 : component is (0.0, 17.5);

    **Fix**

    .. code-block:: vhdl

       attribute coordinate of comp_1 : component is (0.0, 17.5);
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'attribute_specification', '501', lTokens)
        self.groups.append('case::name')
