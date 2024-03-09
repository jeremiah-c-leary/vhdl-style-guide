
from vsg.rules import token_case as Rule

from vsg import token

lTokens = []
lTokens.append(token.iteration_scheme.for_keyword)


class rule_501(Rule):
    '''
    This rule checks the **for** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       FOR x in (31 downto 0) loop

    **Fix**

    .. code-block:: vhdl

       for x in (31 downto 0) loop
    '''

    def __init__(self):
        Rule.__init__(self, lTokens)
        self.groups.append('case::keyword')
