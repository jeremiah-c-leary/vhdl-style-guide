# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.full_type_declaration.is_keyword)


class rule_013(token_case):
    """
    This rule checks the **is** keyword in type definitions has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       type interface IS record
       type interface Is record
       type interface is record

    **Fix**

    .. code-block:: vhdl

       type interface is record
       type interface is record
       type interface is record
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
