# -*- coding: utf-8 -*-

from vsg.rules import (
    align_consecutive_lines_after_line_starting_with_token_and_stopping_with_token as Rule,
)
from vsg.token import report_statement


class rule_400(Rule):
    """
    This rule checks the alignment of the report expressions.

    .. NOTE:: There is a configuration option **alignment** which changes the indent location of multiple lines.

    alignment set to 'report' (Default)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    **Violation**

    .. code-block:: vhdl

       report "FIFO width is limited" &
       " to 16 bits."
         severity FAILURE;

    **Fix**

    .. code-block:: vhdl

       report "FIFO width is limited" &
              " to 16 bits."
         severity FAILURE;

    alignment set to 'left'
    ^^^^^^^^^^^^^^^^^^^^^^^

    **Violation**

    .. code-block:: vhdl

       report "FIFO width is limited" &
       " to 16 bits."
         severity FAILURE;

    **Fix**

    .. code-block:: vhdl

         report "FIFO width is limited" &
             " to 16 bits."
           severity FAILURE;
    """

    def __init__(self):
        Rule.__init__(self)
        self.lStartTokens = [report_statement.report_keyword]
        self.lEndTokens = [report_statement.severity_keyword, report_statement.semicolon]
        self.indentAdjust = 2
        self.configuration_documentation_link = None
