
from vsg.rules import token_case as Rule

from vsg import token

lTokens = []
lTokens.append(token.function_specification.return_keyword)


class rule_501(Rule):
    '''
    This rule checks the **return** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       function overflow (a: integer) RETURN integer is

    **Fix**

    .. code-block:: vhdl

       function overflow (a: integer) return integer is
    '''

    def __init__(self):
        Rule.__init__(self, 'function', '501', lTokens)
        self.groups.append('case::keyword')
