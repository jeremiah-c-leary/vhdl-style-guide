# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_suffix

lTokens = []
lTokens.append(token.component_instantiation_statement.instantiation_label)


class rule_600(token_suffix):
    """
    This rule checks for valid suffixes on instantiation labels.
    The default suffix is *_inst*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       fifo_32x2k : FIFO

    **Fix**

    .. code-block:: vhdl

       fifo_32x2k_inst : FIFO
    """

    def __init__(self):
        super().__init__(lTokens)
        self.suffixes = ["_inst"]
