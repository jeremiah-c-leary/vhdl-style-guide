
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.null_statement.label)
lTokens.append(token.null_statement.null_keyword)


class rule_013(token_indent):
    '''
    This rule checks the indent of the **null** keyword.

    **Violation**

    .. code-block:: vhdl

         when others =>
            null;

         when others =>
       null;

    **Fix**

    .. code-block:: vhdl

       when others =>
         null;

       when others =>
         null;
    '''

    def __init__(self):
        token_indent.__init__(self, 'case', '013', lTokens)
