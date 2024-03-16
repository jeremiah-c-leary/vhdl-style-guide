# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_prefix

lTokens = []
lTokens.append(token.loop_statement.loop_label)


class rule_600(token_prefix):
    """
    This rule checks for valid prefixes on loop labels.
    The default prefix is *loop_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       label : for index in 4 to 23 loop

    **Fix**

    .. code-block:: vhdl

       loop_label : for index in 4 to 23 loop
    """

    def __init__(self):
        super().__init__(lTokens)
        self.prefixes = ["loop_"]
        self.solution = "Loop labels"
