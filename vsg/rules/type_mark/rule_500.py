# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.type_mark.name)


class rule_500(token_case_with_prefix_suffix):
    """
    This rule checks that the name has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

      subtype my_subtype is MY_EXTERNAL_TYPE range 10 to 20;


    **Fix**

    .. code-block:: vhdl

      subtype my_subtype is my_external_type range 10 to 20;

    """

    def __init__(self):
        super().__init__(lTokens)
        self.configuration.append("prefix_exceptions")
        self.configuration.append("suffix_exceptions")
        self.groups.append("case::name")
