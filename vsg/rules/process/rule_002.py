
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.process_statement.process_keyword, token.process_statement.open_parenthesis])
lTokens.append([token.process_statement.process_keyword, token.process_statement.is_keyword])
lTokens.append([token.process_statement.process_keyword, token.process_statement.begin_keyword])


class rule_002(single_space_between_token_pairs):
    '''
    This rule checks for a single space after the **process** keyword.

    **Violation**

    .. code-block:: vhdl

       proc_a : process(rd_en, wr_en, data_in, data_out,

       proc_a : process    (rd_en, wr_en, data_in, data_out,

    **Fix**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,

       proc_a : process (rd_en, wr_en, data_in, data_out,
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'process', '002', lTokens)
        self.solution = 'Ensure a single space after the *process* keyword.'
