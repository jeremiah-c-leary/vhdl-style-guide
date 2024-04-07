# -*- coding: utf-8 -*-

from vsg.rules import token_case_with_prefix_suffix
from vsg.token import architecture_body as token

lTokens = []
lTokens.append(token.architecture_simple_name)


class rule_011(token_case_with_prefix_suffix):
    """
    This rule checks the architecture name case in the **end architecture** statement.

    |configuring_uppercase_and_lowercase_rules_link|


    **Violation**

    .. code-block:: vhdl

       end architecture ARCHITECTURE_NAME;

    **Fix**

    .. code-block:: vhdl

       end architecture architecture_name;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
