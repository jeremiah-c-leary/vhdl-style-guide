# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.block_statement.end_keyword)


class rule_504(token_case):
    """
    This rule checks the **end** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       END block block_label;

    **Fix**

    .. code-block:: vhdl

       end block block_label;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
