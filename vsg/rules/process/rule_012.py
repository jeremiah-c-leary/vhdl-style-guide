
from vsg.rules import insert_token_right_of_possible_tokens_if_it_does_not_exist_before_token

from vsg.token import process_statement as token

oInsertToken = token.is_keyword('is')

lRightTokens = []
lRightTokens.append(token.process_keyword)
lRightTokens.append(token.close_parenthesis)

oBeforeToken = token.begin_keyword


class rule_012(insert_token_right_of_possible_tokens_if_it_does_not_exist_before_token):
    '''
    This rule checks for the existence of the **is** keyword.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       proc_a : process
       begin
       end process;

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        )
       begin
       end process;


    **Fix**

    .. code-block:: vhdl

       proc_a : process is
       begin
       end process;


       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        ) is
       begin
       end process;
    '''

    def __init__(self):
        insert_token_right_of_possible_tokens_if_it_does_not_exist_before_token.__init__(self, 'process', '012', oInsertToken, lRightTokens, oBeforeToken)
        self.solution = '*is* keyword'
        self.groups.append('structure::optional')
