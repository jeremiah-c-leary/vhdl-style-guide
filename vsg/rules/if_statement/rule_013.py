
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.if_statement.else_keyword)


class rule_013(token_indent):
    '''
    This rule checks the indent of the **else** keyword.

    **Violation**

    .. code-block:: vhdl

      if (a = '1') then
        b <= '0'
      elsif (c = '1') then
        d <= '1';
        else
        e <= '0';
      end if;

    **Fix**

    .. code-block:: vhdl

      if (a = '1') then
        b <= '0'
      elsif (c = '1') then
        d <= '1';
      else
        e <= '0';
      end if;
    '''

    def __init__(self):
        token_indent.__init__(self, 'if', '013', lTokens)
