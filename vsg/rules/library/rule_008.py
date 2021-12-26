
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.use_clause.keyword)


class rule_008(token_indent):
    '''
    This rule checks the indent of the **use** keyword.

    **Violation**

    .. code-block:: vhdl

       library ieee;
       use ieee.std_logic_1164.all;
            use ieee.std_logic_unsigned.all;

    **Fix**

    .. code-block:: vhdl

       library ieee;
         use ieee.std_logic_1164.all;
         use ieee.std_logic_unsigned.all;
    '''

    def __init__(self):
        token_indent.__init__(self, 'library', '008', lTokens)
