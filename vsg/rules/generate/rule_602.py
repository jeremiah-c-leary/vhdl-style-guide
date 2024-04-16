# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_suffix_between_tokens

lTokens = []
lTokens.append(token.parameter_specification.identifier)


class rule_602(token_suffix_between_tokens):
    """
    This rule checks for valid suffixes on generate parameter identifiers.
    The default generate suffix is *_gv*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

      gen_label : for index in t_range generate

    **Fix**

    .. code-block:: vhdl

      gen_label : for index_gv in t_range generate
    """

    def __init__(self):
        super().__init__(lTokens, token.for_generate_statement.for_keyword, token.parameter_specification.in_keyword)
        self.suffixes = ["_gv"]
