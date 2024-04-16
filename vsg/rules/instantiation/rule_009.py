# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.instantiated_unit.component_name)


class rule_009(token_case_with_prefix_suffix):
    """
    This rule checks the component name has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       u_fifo : FIFO


    **Fix**

    .. code-block:: vhdl

       u_fifo : fifo
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
