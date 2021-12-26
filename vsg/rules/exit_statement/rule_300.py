
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.exit_statement.label)
lTokens.append(token.exit_statement.exit_keyword)


class rule_300(token_indent):
    '''
    This rule checks the indent of the **exit** keyword.

    **Violation**

    .. code-block:: vhdl

       end if;

         exit;

    **Fix**

    .. code-block:: vhdl

       end if;

       exit;
    '''

    def __init__(self):
        token_indent.__init__(self, 'exit_statement', '300', lTokens)
