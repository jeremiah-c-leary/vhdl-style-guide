
from vsg import token

from vsg.rules import whitespace_before_token as Rule

lTokens = []
lTokens.append(token.loop_statement.loop_keyword)


class rule_102(Rule):
    '''
    This rule checks for a single space before the **loop** keyword.

    **Violation**

    .. code-block:: vhdl

      for x in (0 to 30)loop
      for x in (0 to 30)         loop

    **Fix**

    .. code-block:: vhdl

      for x in (0 to 30) loop
      for x in (0 to 30) loop
    '''
    def __init__(self):
        Rule.__init__(self, 'loop_statement', '102', lTokens)
