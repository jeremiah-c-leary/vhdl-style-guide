
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.process_statement.label_colon, token.process_statement.process_keyword])


class rule_025(Rule):
    '''
    This rule checks for a single space after the colon and before the **process** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       proc_a :process (rd_en, wr_en, data_in, data_out,
                        rd_full, wr_full
                       ) is begin

    **Fix**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        ) is
       begin
    '''
    def __init__(self):
        Rule.__init__(self, 'process', '025', lTokens)
