# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.logical_operator.and_operator)
lTokens.append(token.logical_operator.or_operator)
lTokens.append(token.logical_operator.nand_operator)
lTokens.append(token.logical_operator.nor_operator)
lTokens.append(token.logical_operator.xor_operator)
lTokens.append(token.logical_operator.xnor_operator)


class rule_500(token_case):
    """
    This rule checks logical operators have proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       a <= b AND c;

    **Fix**

    .. code-block:: vhdl

       a <= b and c;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
