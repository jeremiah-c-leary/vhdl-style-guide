# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.context_declaration.identifier)


class rule_012(token_case_with_prefix_suffix):
    """
    This rule checks the context identifier has proper case in the context declaration.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       context C1 is

    **Fix**

    .. code-block:: vhdl

       context c1 is
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
