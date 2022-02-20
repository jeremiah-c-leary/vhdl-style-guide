
from vsg import parser
from vsg import token

from vsg.rules import single_space_after_token as Rule

lTokens = []
lTokens.append(token.if_statement.elsif_keyword)


class rule_005(Rule):
    '''
    This rule checks for a single space after the **elsif** keyword.

    **Violation**

    .. code-block:: vhdl

      elsif(c = '1') then

      elsif   (c = '1') then

      elsif    b = '0' then

    **Fix**

    .. code-block:: vhdl

      elsif (c = '1') then

      elsif (c = '1') then

      elsif b = '0' then
    '''
    def __init__(self):
        Rule.__init__(self, 'if', '005', lTokens)
        self.solution = 'Ensure only a single space exists after the *elsif* keyword.'
