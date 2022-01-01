
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.concurrent_procedure_call_statement.postponed_keyword)


class rule_301(token_indent):
    '''
    This rule checks the indent of the **postponed** keyword if it exists..

    **Violation**

    .. code-block:: vhdl

       a <= b;

         postponed WR_EN(parameter);

    **Fix**

    .. code-block:: vhdl

       a <= b;

       postponed WR_EN(parameter);
    '''

    def __init__(self):
        token_indent.__init__(self, 'procedure_call', '301', lTokens)
