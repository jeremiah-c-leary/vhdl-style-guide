
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.process_statement.begin_keyword)


class rule_022(blank_line_below_line_ending_with_token):
    '''
    This rule checks for a blank line below the **begin** keyword.

    Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

    **Violation**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        ) is
       begin
         rd_en <= '0';

    **Fix**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        ) is
       begin

         rd_en <= '0';
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'process', '022', lTokens)
