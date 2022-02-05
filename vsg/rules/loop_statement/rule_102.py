
from vsg import token

from vsg.rules import single_space_before_token

lTokens = []
lTokens.append(token.loop_statement.loop_keyword)


class rule_102(single_space_before_token):
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
        single_space_before_token.__init__(self, 'loop_statement', '102', lTokens)
