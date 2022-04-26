
from vsg.rules import remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace

from vsg.token import report_statement as token


class rule_001(remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace):
    '''
    This rule removes labels on report_statement_statements.

    **Violation**

    .. code-block:: vhdl

        REPORT_LABEL : report "FIFO width is limited to 16 bits.";

    **Fix**

    .. code-block:: vhdl

        report "FIFO width is limited to 16 bits.";
    '''

    def __init__(self):
        remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace.__init__(self, 'report_statement', '001', token.label, token.label_colon)
        self.solution = 'Remove Label'
