
from vsg import token

from vsg.rules import single_space_after_token

lTokens = []
lTokens.append(token.report_statement.severity_keyword)


class rule_101(single_space_after_token):
    '''
    This rule checks for a single space after the **severity** keyword.

    **Violation**

    .. code-block:: vhdl

        report "FIFO width is limited to 16 bits."
          severity    FAILURE;

    **Fix**

    .. code-block:: vhdl

        report "FIFO width is limited to 16 bits."
          severity FAILURE;
    '''
    def __init__(self):
        single_space_after_token.__init__(self, 'report_statement', '101', lTokens)
