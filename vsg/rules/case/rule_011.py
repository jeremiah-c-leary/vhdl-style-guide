# -*- coding: utf-8 -*-

from vsg.rules import (
    align_consecutive_lines_after_line_starting_with_token_and_stopping_with_token as Rule,
)
from vsg.token import case_statement_alternative as token


class rule_011(Rule):
    """
    This rule checks the alignment of multiline **when** statements.

    **Violation**

    .. code-block:: vhdl

       case data is

         when 0 | 1 | 2 | 3
          4 | 5 | 7 =>

    **Fix**

    .. code-block:: vhdl

       case data is

         when 0 | 1 | 2 | 3
              4 | 5 | 7 =>
    """

    def __init__(self):
        Rule.__init__(self)
        self.lStartTokens = [token.when_keyword]
        self.lEndTokens = [token.assignment]
        self.solution = "Align one space after *when* keyword"
        self.configuration_documentation_link = None
