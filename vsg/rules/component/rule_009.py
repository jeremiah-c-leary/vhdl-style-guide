
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.component_declaration.end_keyword)


class rule_009(token_indent):
    '''
    This rule checks the indent of the **end component** keywords.

    **Violation**

    .. code-block:: vhdl

          overflow : std_logic
        );
            end component fifo;

    **Fix**

    .. code-block:: vhdl

           overflow : std_logic
         );
       end component fifo;
    '''

    def __init__(self):
        token_indent.__init__(self, 'component', '009', lTokens)
