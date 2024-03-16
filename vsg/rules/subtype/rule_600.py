# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_suffix

lTokens = []
lTokens.append(token.subtype_declaration.identifier)


class rule_600(token_suffix):
    """
    This rule checks for valid suffixes in subtype identifiers.
    The default new subtype suffix is *_st*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       subtype my_subtype is range 0 to 9;

    **Fix**

    .. code-block:: vhdl

       subtype my_subtype_st is range 0 to 9;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.suffixes = ["_st"]
