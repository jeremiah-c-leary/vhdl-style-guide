# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_prefix_between_tokens

lTokens = []
lTokens.append(token.parameter_specification.identifier)


class rule_601(token_prefix_between_tokens):
    """
    This rule checks for valid prefixes on generate parameter identifiers.
    The default generate prefix is *gv_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

      gen_label : for index in t_range generate

    **Fix**

    .. code-block:: vhdl

      gen_label : for gv_index in t_range generate
    """

    def __init__(self):
        super().__init__(lTokens, token.for_generate_statement.for_keyword, token.parameter_specification.in_keyword)
        self.prefixes = ["gv_"]
