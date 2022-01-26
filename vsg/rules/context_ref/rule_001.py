
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.context_reference.keyword)


class rule_001(token_indent):
    '''
    This rule checks the indent of the **context** keyword.

    **Violation**

    .. code-block:: vhdl

       library ieee;
       context c1;

    **Fix**

    .. code-block:: vhdl

       library ieee;
         context c1;
    '''

    def __init__(self):
        token_indent.__init__(self, 'context_ref', '001', lTokens)
