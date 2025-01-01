# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import n_spaces_before_and_after_tokens

lTokens = []
lTokens.append(token.shift_operator.sll)
lTokens.append(token.shift_operator.srl)
lTokens.append(token.shift_operator.sla)
lTokens.append(token.shift_operator.sra)
lTokens.append(token.shift_operator.rol)
lTokens.append(token.shift_operator.ror)


class rule_101(n_spaces_before_and_after_tokens):
    """
    This rule checks for at least a single space before and after logical operators.

    **Violation**

    .. code-block:: vhdl

      if (a = '1')sll(b = '0')
      if (a = '0')rol (b = '1')

    **Fix**

    .. code-block:: vhdl

      if (a = '1') sll (b = '0')
      if (a = '0') rol (b = '1')
    """

    def __init__(self):
        super().__init__(1, lTokens, bNIsMinimum=True)
        self.solution = "Ensure a single space before and after shift operator."
        self.configuration_documentation_link = None
