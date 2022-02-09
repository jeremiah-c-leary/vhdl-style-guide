
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.ieee.std_logic_1164.types.std_logic)
lTokens.append(token.ieee.std_logic_1164.types.std_logic_vector)
lTokens.append(token.ieee.std_logic_1164.types.std_ulogic)
lTokens.append(token.ieee.std_logic_1164.types.std_ulogic_vector)
lTokens.append(token.ieee.std_logic_1164.types.integer)
lTokens.append(token.ieee.std_logic_1164.types.signed)
lTokens.append(token.ieee.std_logic_1164.types.unsigned)


class rule_500(token_case):
    '''
    This rule checks IEEE types have the proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       port (
         WR_EN    : in    STD_LOGIC;
         RD_EN    : in    STD_logic;
         DATA     : inout STD_LOGIC_VECTOR(31 downto 0)
       );

    **Fix**

    .. code-block:: vhdl

       port (
         WR_EN    : in    std_logic;
         RD_EN    : in    std_logic;
         DATA     : inout std_logic_vector(31 downto 0)
       );
    '''

    def __init__(self):
        token_case.__init__(self, 'ieee', '500', lTokens)
        self.groups.append('case::keyword')
