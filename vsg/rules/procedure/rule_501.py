# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.procedure_specification.designator)


class rule_501(token_case_with_prefix_suffix):
    """
    This rule checks the procedure designator has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       procedure AVERAGE_SAMPLES is

    **Fix**

    .. code-block:: vhdl

       procedure average_samples is
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
