
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.context_declaration.end_keyword)


class rule_020(token_indent):
    '''
    This rule checks the indent of the **end** keyword.

    **Violation**

    .. code-block:: vhdl

       context c1 is
          end context c1;

    **Fix**

    .. code-block:: vhdl

       context c1 is
       end context c1;
    '''

    def __init__(self):
        token_indent.__init__(self, 'context', '020', lTokens)
