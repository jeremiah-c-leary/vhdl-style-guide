# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import multiline_subprogram_specification_structure as Rule

oSubprogramSpecification = token.function_specification

lTokenPairs = []
lTokenPairs.append([token.function_specification.function_keyword, token.function_specification.close_parenthesis])


class rule_019(Rule):
    """
    This rule checks the structure of function specifications.

    |configuring_subprogram_specification_statement_rules_link|

    **Violation**

    .. code-block:: vhdl

        function average_samples (num_samples : in integer; sample : out std_logic) return integer;

    **Fix**

    .. code-block:: vhdl

        function average_samples (
          num_samples : in integer;
          sample      : out std_logic
        ) return integer;
    """

    def __init__(self):
        Rule.__init__(self)
        self.lTokenPairs = lTokenPairs
        self.oSubprogramSpecification = oSubprogramSpecification
