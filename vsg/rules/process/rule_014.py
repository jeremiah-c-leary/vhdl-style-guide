
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.process_statement.process_keyword, token.process_statement.is_keyword])
lTokens.append([token.process_statement.close_parenthesis, token.process_statement.is_keyword])


class rule_014(Rule):
    '''
    This rule checks for a single space before the **is** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        )     is
       begin

    **Fix**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        ) is
       begin
    '''
    def __init__(self):
        Rule.__init__(self, 'process', '014', lTokens)
