
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.process_statement.process_label)


class rule_017(token_case_with_prefix_suffix):
    '''
    This rule checks the process label has proper case.
    
    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.
    
    **Violation**
    
    .. code-block:: vhdl
    
       PROC_A : process (rd_en, wr_en, data_in, data_out,
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
        token_case_with_prefix_suffix.__init__(self, 'process', '017', lTokens)
        self.groups.append('case::label')
