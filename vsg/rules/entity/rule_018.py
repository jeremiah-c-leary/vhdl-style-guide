
from vsg.rules import align_tokens_in_region_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.interface_unknown_declaration.assignment)


class rule_018(align_tokens_in_region_between_tokens):
    '''
    This rule checks the alignment of **:=** operator for each generic and port in the entity declaration.

    Following extra configurations are supported:

    * :code:`separate_generic_port_alignment`.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       generic (
           g_width        : positive := 8;
           g_output_delay : positive      := 5
       );
       port (
           clk_i   : in std_logic;
           data1_i : in std_logic  := 'X';
           data2_i : in std_logic      := 'X';
           data_o  : in std_logic
       );

    **Fix**

    .. code-block:: vhdl

       generic (
           g_width        : positive := 8;
           g_output_delay : positive := 5
       );
       port (
           clk_i   : in std_logic;
           data1_i : in std_logic := 'X';
           data2_i : in std_logic := 'X';
           data_o  : in std_logic
       );
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens.__init__(self, 'entity', '018', lAlign, token.entity_declaration.entity_keyword, token.entity_declaration.end_keyword)
        self.solution = 'Align :.'
