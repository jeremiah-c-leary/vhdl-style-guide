
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.library_clause.keyword)


class rule_001(token_indent):
    '''
    This rule checks the indent of the **library** keyword.
    Indenting helps in comprehending the code.


    **Violation**

    .. code-block:: vhdl

       library ieee;
          library fifo_dsn;

    **Fix**

    .. code-block:: vhdl

       library ieee;
       library fifo_dsn;
    '''

    def __init__(self):
        token_indent.__init__(self, 'library', '001', lTokens)
