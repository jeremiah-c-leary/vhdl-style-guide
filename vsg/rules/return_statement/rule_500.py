
from vsg.rules import token_case as Rule

from vsg import token

lTokens = []
lTokens.append(token.return_statement.return_keyword)


class rule_500(Rule):
    '''
    This rule checks the **return** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       RETURN my_value;

    **Fix**

    .. code-block:: vhdl

       return my_value;
    '''

    def __init__(self):
        Rule.__init__(self, 'return_statement', '500', lTokens)
        self.groups.append('case::keyword')
