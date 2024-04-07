# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_suffix

lTokens = []
lTokens.append(token.loop_statement.loop_label)


class rule_601(token_suffix):
    """
    This rule checks for valid suffixes on loop labels.
    The default prefix is *_loop*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       label : for index in 4 to 23 loop

    **Fix**

    .. code-block:: vhdl

       label_loop : for index in 4 to 23 loop
    """

    def __init__(self):
        super().__init__(lTokens)
        self.suffixes = ["_loop"]
        self.solution = "Loop labels"
