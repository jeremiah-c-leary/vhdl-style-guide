
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.report_statement.report_keyword)
lTokens.append(token.report_statement.severity_keyword)


class rule_300(token_indent):
    '''
    This rule checks indent of multiline report statements.

    **Violation**

    .. code-block:: vhdl

        report "FIFO width is limited to 16 bits."
                severity FAILURE;

    **Fix**

    .. code-block:: vhdl

        report "FIFO width is limited to 16 bits."
          severity FAILURE;
    '''

    def __init__(self):
        token_indent.__init__(self, 'report_statement', '300', lTokens)
