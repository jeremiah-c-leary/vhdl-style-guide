# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.attribute_declaration.identifier)


class rule_501(token_case_with_prefix_suffix):
    """
    This rule checks the *identifier* has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       attribute MAX_DELAY : time;

    **Fix**

    .. code-block:: vhdl

       attribute max_delay : time;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
