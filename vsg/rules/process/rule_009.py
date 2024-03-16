# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.process_statement.end_process_keyword)


class rule_009(token_case):
    """
    This rule checks the **process** keyword has proper case in the **end process** line.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end PROCESS proc_a;

    **Fix**

    .. code-block:: vhdl

       end process proc_a;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
