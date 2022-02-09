
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.process_statement.process_keyword)


class rule_005(token_case):
    '''
    This rule checks the **process** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       proc_a : PROCESS (rd_en, wr_en, data_in, data_out,

    **Fix**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
    '''

    def __init__(self):
        token_case.__init__(self, 'process', '005', lTokens)
        self.groups.append('case::keyword')
