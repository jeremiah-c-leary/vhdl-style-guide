# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.direction.to)


class rule_002(token_case):
    """
    This rule checks the case of the **to** keyword.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       signal sig1 : std_logic_vector(3 TO 0);
       signal sig2 : std_logic_vector(16 tO 1);

    **Fix**

    .. code-block:: vhdl

       signal sig1 : std_logic_vector(3 to 0);
       signal sig2 : std_logic_vector(16 to 1);
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
