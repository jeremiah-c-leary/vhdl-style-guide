
from vsg.token import assertion
from vsg.token import assertion_statement
from vsg.token import concurrent_assertion_statement

from vsg.rules import align_consecutive_lines_after_line_starting_with_token_and_stopping_with_token as Rule


class rule_400(Rule):
    '''
    This rule checks the alignment of the report expressions.

    .. NOTE:: There is a configuration option **alignment** which changes the indent location of multiple lines.

    |configuring_multiline_report_rule_link|

    **Violation**

    .. code-block:: vhdl

       assert WIDTH > 16
         report "FIFO width is limited" &
       " to 16 bits."
         severity FAILURE;

    **Fix**

    .. code-block:: vhdl

       assert WIDTH > 16
         report "FIFO width is limited" &
                " to 16 bits."
         severity FAILURE;
    '''

    def __init__(self):
        Rule.__init__(self, name="assert", identifier="400")
        self.lStartTokens = [assertion.report_keyword]
        self.lEndTokens = [assertion.severity_keyword, assertion_statement.semicolon, concurrent_assertion_statement.semicolon]
