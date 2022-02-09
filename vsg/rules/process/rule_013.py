
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.process_statement.is_keyword)


class rule_013(token_case):
    '''
    This rule checks the **is** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

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
