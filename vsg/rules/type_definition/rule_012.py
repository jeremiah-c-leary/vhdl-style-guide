
from vsg.rules import token_indent_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.identifier_list.identifier)

oStart = token.record_type_definition.record_keyword
oEnd = token.record_type_definition.end_keyword

class rule_012(token_indent_between_tokens):
    '''
    This rule checks the indent of record elements in record type declarations.

    **Violation**

    .. code-block:: vhdl

       type interface is record
         data : std_logic_vector(31 downto 0);
       chip_select : std_logic;
           wr_en : std_logic;
       end record;

    **Fix**

    .. code-block:: vhdl

       type interface is record
         data : std_logic_vector(31 downto 0);
         chip_select : std_logic;
         wr_en : std_logic;
       end record;
    '''

    def __init__(self):
        token_indent_between_tokens.__init__(self, 'type', '012', lTokens, oStart, oEnd)
