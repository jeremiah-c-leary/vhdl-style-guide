# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_in_range_bounded_by_tokens

lTokens = []
lTokens.append(token.type_mark.name)

oStartToken = token.attribute_declaration.colon

oEndToken = token.attribute_declaration.semicolon


class rule_502(token_case_in_range_bounded_by_tokens):
    """
    This rule checks the *type_mark* has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       attribute max_delay : TIME;

    **Fix**

    .. code-block:: vhdl

       attribute max_delay : time;
    """

    def __init__(self):
        super().__init__(lTokens, oStartToken, oEndToken)
        self.groups.append("case::name")
        self.configuration.append("case_exceptions")
