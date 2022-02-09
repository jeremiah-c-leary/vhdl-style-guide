
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.alias_declaration.alias_designator)


class rule_502(token_case_with_prefix_suffix):
    '''
    This rule checks the alias designator has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       alias Alias_Designator is name;

    **Fix**

    .. code-block:: vhdl

       alias alias_designator is name;
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'alias_declaration', '502', lTokens)
        self.groups.append('case::name')
