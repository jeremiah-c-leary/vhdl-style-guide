# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_suffix

lTokens = []
lTokens.append(token.incomplete_type_declaration.identifier)
lTokens.append(token.full_type_declaration.identifier)


class rule_600(token_suffix):
    """
    This rule checks for valid suffixes in user defined type identifiers.
    The default new type suffix is *_t*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       type my_type is range -5 to 5 ;

    **Fix**

    .. code-block:: vhdl

       type my_type_t is range -5 to 5 ;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.suffixes = ["_t"]
        self.solution = "Type identifiers"
