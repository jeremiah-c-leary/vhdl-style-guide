# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.component_declaration.identifier)


class rule_008(token_case_with_prefix_suffix):
    """
    This rule checks the component name has proper case in the component declaration.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       component FIFO is

    **Fix**

    .. code-block:: vhdl

       component fifo is
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
