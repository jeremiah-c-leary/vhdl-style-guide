# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_suffix

lTokens = []
lTokens.append(token.function_specification.designator)


class rule_601(token_suffix):
    """
    This rule checks for valid suffixes on function designators.
    Default signal suffix is *_f*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       function read_data

    **Fix**

    .. code-block:: vhdl

       function read_data_f
    """

    def __init__(self):
        super().__init__(lTokens)
        self.suffixes = ["_f"]
        self.solution = "Function designator"
