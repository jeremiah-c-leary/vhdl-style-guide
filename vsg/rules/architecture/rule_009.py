# -*- coding: utf-8 -*-

from vsg.rules import token_case
from vsg.token import architecture_body as token


class rule_009(token_case):
    """
    This rule checks the **end** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       END architecture;

       End architecture;

    **Fix**

    .. code-block:: vhdl

       end architecture;

       end architecture;
    """

    def __init__(self):
        super().__init__([token.end_keyword])
        self.groups.append("case::keyword")
