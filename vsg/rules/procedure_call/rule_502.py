# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_in_range_bounded_by_tokens as Rule

lTokens = []
lTokens.append(token.association_element.formal_part)


class rule_502(Rule):
    """
    This rule checks that the parameter names have proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl


      my_proc (
        PARAM1 => MY_PARAM1,
        PaRaM2 => MY_PARAM2
      );

    **Fix**

    .. code-block:: vhdl

      my_proc (
        param1 => MY_PARAM1,
        param2 => MY_PARAM2
      );
    """

    def __init__(self):
        super().__init__(lTokens, token.procedure_call.open_parenthesis, token.procedure_call.close_parenthesis)
        self.configuration.append("prefix_exceptions")
        self.configuration.append("suffix_exceptions")
        self.configuration.append("case_exceptions")
        self.groups.append("case::name")
