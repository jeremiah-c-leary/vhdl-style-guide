# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_suffix as Rule

lTokens = []
lTokens.append(token.alias_declaration.alias_designator)


class rule_601(Rule):
    """
    This rule checks for valid suffixes on alias designators.

    Default prefix is *_a*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       alias header is name;
       alias footer is name;

    **Fix**

    .. code-block:: vhdl

       alias header_a is name;
       alias footer_a is name;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.suffixes = ["_a"]
        self.solution = "Alias designators"
