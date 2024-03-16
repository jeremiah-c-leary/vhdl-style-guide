# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import multiline_subprogram_specification_structure as Rule

oSubprogramSpecification = token.procedure_specification

lTokenPairs = []
lTokenPairs.append([token.procedure_specification.procedure_keyword, token.procedure_specification.close_parenthesis])


class rule_013(Rule):
    """
    This rule checks the structure of procedure specifications.

    |configuring_subprogram_specification_statement_rules_link|

    **Violation**

    .. code-block:: vhdl

        procedure average_samples (num_samples : in integer; sample : out std_logic);

    **Fix**

    .. code-block:: vhdl

        procedure average_samples (
          num_samples : in integer;
          sample      : out std_logic
        );
    """

    def __init__(self):
        Rule.__init__(self)
        self.lTokenPairs = lTokenPairs
        self.oSubprogramSpecification = oSubprogramSpecification
