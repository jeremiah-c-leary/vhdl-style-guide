# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_suffix_between_tokens

lTokens = []
lTokens.append(token.parameter_specification.identifier)


class rule_603(token_suffix_between_tokens):
    """
    This rule checks for valid suffixes on loop parameter identifiers.
    The default loop suffix is *_lv*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

      for index in t_range loop

    **Fix**

    .. code-block:: vhdl

      for index_lv in t_range loop
    """

    def __init__(self):
        super().__init__(lTokens, token.iteration_scheme.for_keyword, token.parameter_specification.in_keyword)
        self.suffixes = ["_lv"]
