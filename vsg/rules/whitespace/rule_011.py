# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import n_spaces_before_and_after_tokens

lTokens = []
lTokens.append(token.adding_operator.plus)
lTokens.append(token.adding_operator.minus)
lTokens.append(token.multiplying_operator.star)
lTokens.append(token.multiplying_operator.slash)
lTokens.append(token.miscellaneous_operator.double_star)


class rule_011(n_spaces_before_and_after_tokens):
    r"""
    This rule checks for at least a single space before and after math operators +, -, /, * and \*\*.

    **Violation**

    .. code-block:: vhdl

       a <= b+c;
       a <= b-c;
       a <= b/c;
       a <= b*c;
       a <= b**c;
       a <= (b+c)-(d-e);

    **Fix**

    .. code-block:: vhdl

       a <= b + c;
       a <= b - c;
       a <= b / c;
       a <= b * c;
       a <= b ** c;
       a <= (b + c) - (d - e);
    """

    def __init__(self):
        super().__init__(1, lTokens, bNIsMinimum=True)
        self.solution = "Ensure at least a single space before and after math operator."
        self.configuration_documentation_link = None
