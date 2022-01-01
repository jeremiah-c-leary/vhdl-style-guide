
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.assertion.keyword)
lTokens.append(token.assertion.report_keyword)
lTokens.append(token.assertion.severity_keyword)
lTokens.append(token.concurrent_assertion_statement.label_name)
lTokens.append(token.assertion_statement.label)


class rule_001(token_indent):
    '''
    This rule checks indent of multiline assert statements.

    **Violation**

    .. code-block:: vhdl

       assert WIDTH > 16
            report "FIFO width is limited to 16 bits."
        severity FAILURE;

    **Fix**

    .. code-block:: vhdl

       assert WIDTH > 16
         report "FIFO width is limited to 16 bits."
         severity FAILURE;
    '''

    def __init__(self):
        token_indent.__init__(self, 'assert', '001', lTokens)
