# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_prefix

lTokens = []
lTokens.append(token.subtype_declaration.identifier)


class rule_004(token_prefix):
    """
    This rule checks for valid prefixes in subtype identifiers.
    The default new subtype prefix is *st_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       subtype my_subtype is range 0 to 9;

    **Fix**

    .. code-block:: vhdl

       subtype st_my_subtype is range 0 to 9;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.prefixes = ["st_"]
