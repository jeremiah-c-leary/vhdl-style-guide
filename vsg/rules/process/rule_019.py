# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.process_statement.end_process_label)


class rule_019(token_case_with_prefix_suffix):
    """
    This rule checks the **end process** label has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end process PROC_A;

    **Fix**

    .. code-block:: vhdl

       end process proc_a;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::label")
