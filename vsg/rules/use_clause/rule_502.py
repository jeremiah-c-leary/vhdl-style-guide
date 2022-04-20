
from vsg.rules import token_case as Rule

from vsg import token

lTokens = []
lTokens.append(token.use_clause.item_name)


class rule_502(Rule):
    '''
    This rule checks the item name called out in the selected name has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       use my_lib.Increment;

    **Fix**

    .. code-block:: vhdl

       use my_lib.increment;
    '''

    def __init__(self):
        Rule.__init__(self, 'use_clause', '502', lTokens)
        self.groups.append('case::name')
        self.configuration.append('case_exceptions')
