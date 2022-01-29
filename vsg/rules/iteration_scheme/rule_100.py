
from vsg.rules import single_space_after_token as Rule

from vsg.token import iteration_scheme as token

lTokens = []
lTokens.append(token.while_keyword)


class rule_100(Rule):
    '''
    This rule checks that a single space exists after the **while** keyword.

    **Violation**

    .. code-block:: vhdl

       while(condition)

       while      (condition)

    **Fix**

    .. code-block:: vhdl

       while (condition)

       while (condition)
    '''
    def __init__(self):
        Rule.__init__(self, 'iteration_scheme', '100', lTokens)
        self.solution = 'Ensure a single space after while.'
