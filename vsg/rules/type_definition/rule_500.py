# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.enumeration_type_definition.enumeration_literal)


class rule_500(token_case):
    """
    This rule checks enumerate types have proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       type state_machine is (IDLE, WRITE, READ, DONE);

    **Fix**

    .. code-block:: vhdl

       type state_machine is (idle, write, read, done);
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
