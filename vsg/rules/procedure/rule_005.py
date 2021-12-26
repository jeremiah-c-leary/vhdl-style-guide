
from vsg.rules import token_indent_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.use_clause.keyword)
lTokens.append(token.variable_declaration.variable_keyword)
lTokens.append(token.constant_declaration.constant_keyword)

oStart = token.subprogram_body.is_keyword
oEnd = token.subprogram_body.begin_keyword


class rule_005(token_indent_between_tokens):
    '''
    This rule checks the indent of lines between the **is** and **begin** keywords

    **Violation**

    .. code-block:: vhdl

       procedure average_samples (
         constant a : in integer;
         signal d : out std_logic ) is
       variable var_1 : integer;
           variable var_1 : integer;
       begin
       end procedure average_samples;


    **Fix**

    .. code-block:: vhdl

       procedure average_samples (
         constant a : in integer;
         signal b : in std_logic;
         variable c : in std_logic_vector(3 downto 0);
         signal d : out std_logic ) is
         variable var_1 : integer;
         variable var_1 : integer;
       begin
       end procedure average_samples;
    '''

    def __init__(self):
        token_indent_between_tokens.__init__(self, 'procedure', '005', lTokens, oStart, oEnd)
