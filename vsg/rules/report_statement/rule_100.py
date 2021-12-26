
from vsg import token

from vsg.rules import single_space_after_token

lTokens = []
lTokens.append(token.report_statement.report_keyword)


class rule_100(single_space_after_token):
    '''
    This rule checks for a single space after the **report** keyword.

    **Violation**

    .. code-block:: vhdl

        report     "FIFO width is limited to 16 bits.";

    **Fix**

    .. code-block:: vhdl

        report "FIFO width is limited to 16 bits.";
    '''
    def __init__(self):
        single_space_after_token.__init__(self, 'report_statement', '100', lTokens)
