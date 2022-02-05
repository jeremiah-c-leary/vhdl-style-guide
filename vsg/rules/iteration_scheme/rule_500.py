
from vsg.rules import token_case as Rule

from vsg import token

lTokens = []
lTokens.append(token.iteration_scheme.while_keyword)


class rule_500(Rule):
    '''
    This rule checks the **while** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       WHILE (condition) loop

    **Fix**

    .. code-block:: vhdl

       while (condition) loop
    '''

    def __init__(self):
        Rule.__init__(self, 'iteration_scheme', '500', lTokens)
        self.groups.append('case::keyword')
