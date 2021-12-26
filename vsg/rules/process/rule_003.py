
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.process_statement.begin_keyword)


class rule_003(token_indent):
    '''
    This rule checks the indent of the **begin** keyword.

    **Violation**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        ) is
         begin

    **Fix**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        ) is
       begin
    '''

    def __init__(self):
        token_indent.__init__(self, 'process', '003', lTokens)
