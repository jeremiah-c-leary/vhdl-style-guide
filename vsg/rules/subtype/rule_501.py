# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.subtype_declaration.identifier)


class rule_501(token_case):
    """
    This rule checks the identifier has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       subtype INTERFACE is record
       subtype Interface is record
       subtype interface is record

    **Fix**

    .. code-block:: vhdl

       subtype interface is record
       subtype interface is record
       subtype interface is record
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
