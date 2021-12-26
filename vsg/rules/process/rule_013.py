
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.process_statement.is_keyword)


class rule_013(token_case):
    '''
    This rule checks the **is** keyword has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        ) IS
       begin

    **Fix**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        ) is
       begin
    '''

    def __init__(self):
        token_case.__init__(self, 'process', '013', lTokens)
        self.groups.append('case::keyword')
