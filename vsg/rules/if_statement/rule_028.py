# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.if_statement.end_keyword)


class rule_028(token_case):
    """
    This rule checks the **end** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       END if;

       End if;

    **Fix**

    .. code-block:: vhdl

       end if;

       end if;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
