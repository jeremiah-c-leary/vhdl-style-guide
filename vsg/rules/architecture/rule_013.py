# -*- coding: utf-8 -*-

from vsg.rules import token_case_with_prefix_suffix
from vsg.token import architecture_body as token

lTokens = []
lTokens.append(token.identifier)


class rule_013(token_case_with_prefix_suffix):
    """
    This rule checks the case of the architecture name in the architecture declaration.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       architecture RTL of fifo is

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
