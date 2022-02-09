
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.entity_name_list.all_keyword)


class rule_501(token_case):
    '''
    This rule checks the **all** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       attribute coordinate of ALL : component is (0.0, 17.5);

    **Fix**

    .. code-block:: vhdl

       attribute coordinate of all : component is (0.0, 17.5);
    '''

    def __init__(self):
        token_case.__init__(self, 'entity_specification', '501', lTokens)
        self.groups.append('case::keyword')
