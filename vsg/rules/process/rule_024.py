
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.process_statement.process_label, token.process_statement.label_colon])


class rule_024(Rule):
    '''
    This rule checks for a single space after the process label.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       proc_a: process (rd_en, wr_en, data_in, data_out,
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
        Rule.__init__(self, 'process', '024', lTokens)
