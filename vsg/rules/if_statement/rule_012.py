# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.if_statement.elsif_keyword)


class rule_012(token_indent):
    """
    This rule checks the indent of the **elsif** keyword.

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
    """

    def __init__(self):
        super().__init__(lTokens)
