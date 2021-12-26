
from vsg.rules import align_left_token_with_right_token_if_right_token_starts_a_line

from vsg import token

oLeftToken = token.process_statement.open_parenthesis
oRightToken = token.process_statement.close_parenthesis


class rule_028(align_left_token_with_right_token_if_right_token_starts_a_line):
    '''
    This rule checks the alignment of the closing parenthesis of a sensitivity list.
    Parenthesis on multiple lines should be in the same column.

    **Violation**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                           )

    **Fix**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        )
    '''

    def __init__(self):
        align_left_token_with_right_token_if_right_token_starts_a_line.__init__(self, 'process', '028', oLeftToken, oRightToken)
