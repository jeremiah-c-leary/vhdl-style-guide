
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.process_statement.process_keyword, token.process_statement.open_parenthesis])
lTokens.append([token.process_statement.process_keyword, token.process_statement.is_keyword])
lTokens.append([token.process_statement.process_keyword, token.process_statement.begin_keyword])


class rule_002(Rule):
    '''
    This rule checks for a single space after the **process** keyword.

    |configuring_whitespace_rules_link|

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
        Rule.__init__(self, 'process', '002', lTokens)
