# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.process_statement.process_keyword)


class rule_005(token_case):
    """
    This rule checks the **process** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       proc_a : PROCESS (rd_en, wr_en, data_in, data_out,

    **Fix**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
