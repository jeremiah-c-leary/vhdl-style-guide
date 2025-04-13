# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_prefix

lTokens = []
lTokens.append(token.interface_incomplete_type_declaration.identifier)


class rule_600(token_prefix):
    """
    This rule checks for valid prefixes of type names.

    .. NOTE::  The default prefix is *gt_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       generic (
         type generic_data_type

    **Fix**

    .. code-block:: vhdl

       generic (
         type gt_generic_data_type
    """

    def __init__(self):
        super().__init__(lTokens)
        self.prefixes = ["gt_"]
        self.solution = "Type identifiers"
