# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import n_spaces_before_and_after_tokens

lTokens = []
lTokens.append(token.relational_operator.equal)
lTokens.append(token.relational_operator.not_equal)
lTokens.append(token.relational_operator.less_than)
lTokens.append(token.relational_operator.less_than_or_equal)
lTokens.append(token.relational_operator.greater_than)
lTokens.append(token.relational_operator.greater_than_or_equal)
lTokens.append(token.relational_operator.question_equal)
lTokens.append(token.relational_operator.question_not_equal)
lTokens.append(token.relational_operator.question_less_than)
lTokens.append(token.relational_operator.question_less_than_or_equal)
lTokens.append(token.relational_operator.question_greater_than)
lTokens.append(token.relational_operator.question_greater_than_or_equal)


class rule_100(n_spaces_before_and_after_tokens):
    """
    This rule checks for at least a single space before and after relational operators.

    **Violation**

    .. code-block:: vhdl

      if readAddr>=writeAddr then
      if readAddr    >=      writeAddr then

    **Fix**

    .. code-block:: vhdl

      if readAddr >= writeAddr then
      if readAddr >= writeAddr then
    """

    def __init__(self):
        super().__init__(1, lTokens, bNIsMinimum=False)
        self.solution = "Ensure a single space before and after relational operator."
        self.configuration_documentation_link = None
