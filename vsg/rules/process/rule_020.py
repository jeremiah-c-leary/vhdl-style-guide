
from vsg.rules import multiline_alignment_between_tokens

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.process_statement.open_parenthesis, token.process_statement.close_parenthesis])


class rule_020(multiline_alignment_between_tokens):
    '''
    This rule checks the indentation of multiline sensitivity lists.

    **Violation**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                            rd_full, wr_full,
                   overflow, underflow
                        ) is begin

    **Fix**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full,
                         overflow, underflow
                        ) is
       begin
    '''

    def __init__(self):
        multiline_alignment_between_tokens.__init__(self, 'process', '020', lTokenPairs, True)
