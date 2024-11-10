# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_in_range_bounded_by_tokens as Rule

lTokens = []
lTokens.append(token.interface_constant_declaration.identifier)
lTokens.append(token.interface_signal_declaration.identifier)
lTokens.append(token.interface_variable_declaration.identifier)
lTokens.append(token.interface_unknown_declaration.identifier)
lTokens.append(token.interface_file_declaration.identifier)


class rule_507(Rule):
    """
    This rule checks that the parameter names have proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

      function my_func (
        PARAM1 : in integer;
        PaRaM2 : out integer
      ) return integer;

    **Fix**

    .. code-block:: vhdl

      function my_func (
        param1 : in integer;
        param2 : out integer
      ) return integer;
    """

    def __init__(self):
        super().__init__(lTokens, token.function_specification.open_parenthesis, token.function_specification.close_parenthesis)
        self.configuration.append("prefix_exceptions")
        self.configuration.append("suffix_exceptions")
        self.configuration.append("case_exceptions")
        self.groups.append("case::name")
