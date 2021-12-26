
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.end_keyword)


class rule_003(token_indent):
    '''
    This rule checks the indent of the **end** keyword.

    **Violation**

    .. code-block:: vhdl

       procedure average_samples (
         constant a : in integer;
         signal b : in std_logic;
         variable c : in std_logic_vector(3 downto 0);
         signal d : out std_logic ) is
       begin
         end procedure average_samples;

    **Fix**

    .. code-block:: vhdl

       procedure average_samples (
         constant a : in integer;
         signal b : in std_logic;
         variable c : in std_logic_vector(3 downto 0);
         signal d : out std_logic ) is
       begin
       end procedure average_samples;
    '''

    def __init__(self):
        token_indent.__init__(self, 'procedure', '003', lTokens)
