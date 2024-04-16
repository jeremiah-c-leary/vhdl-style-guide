# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.report_statement.severity_keyword)


class rule_501(token_case):
    """
    This rule checks the **severity** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

        report "FIFO width is limited to 16 bits."
          SEVERITY FAILURE;

    .. code-block:: vhdl

        report "FIFO width is limited to 16 bits."
          severity FAILURE;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
