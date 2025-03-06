# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_suffix

lTokens = []
lTokens.append(token.interface_incomplete_type_declaration.identifier)


class rule_601(token_suffix):
    """
    This rule checks for valid suffixes of type names.

    .. NOTE::  The default prefix is *_gt*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       generic (
         type generic_data_type

    **Fix**

    .. code-block:: vhdl

       generic (
         type generic_data_type_gt
    """

    def __init__(self):
        super().__init__(lTokens)
        self.suffixes = ["_gt"]
        self.solution = "Type identifiers"
