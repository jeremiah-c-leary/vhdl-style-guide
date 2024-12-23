# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.constrained_array_definition.array_keyword)


class rule_500(token_case):
    """
    This rule checks the **array** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       type t_u_array is ARRAY(1 downto 0) of unsigned;

    **Fix**

    .. code-block:: vhdl

       type t_u_array is array(1 downto 0) of unsigned;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
