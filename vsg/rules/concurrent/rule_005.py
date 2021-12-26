
from vsg.rules import remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace

from vsg.token import concurrent_signal_assignment_statement as token


class rule_005(remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace):
    '''
    This rule checks for labels on concurrent assignments.
    Labels on concurrents are optional and do not provide additional information.

    **Violation**

    .. code-block:: vhdl

       WR_EN_OUTPUT : WR_EN <= q_wr_en;
       RD_EN_OUTPUT : RD_EN <= q_rd_en;

    **Fix**

    .. code-block:: vhdl

       WR_EN <= q_wr_en;
       RD_EN <= q_rd_en;
    '''

    def __init__(self):
        remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace.__init__(self, 'concurrent', '005', token.label_name, token.label_colon)
        self.solution = 'Remove Label'
