
from vsg.rules import align_tokens_in_region_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.interface_unknown_declaration.colon)


class rule_017(align_tokens_in_region_between_tokens):
    '''
    This rule checks the alignment of the colon for each generic and port in the component declaration.

    Following extra configurations are supported:

    * :code:`separate_generic_port_alignment`.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       component my_component
           generic (
               g_width : positive;
               g_output_delay : positive
           );
           port (
               clk_i : in std_logic;
               data_i : in std_logic;
               data_o : in std_logic
           );
       end component;

    **Fix**

    .. code-block:: vhdl

       component my_component
           generic (
               g_width        : positive;
               g_output_delay : positive
           );
           port (
               clk_i  : in std_logic;
               data_i : in std_logic;
               data_o : in std_logic
           );
       end component;
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens.__init__(self, 'component', '017', lAlign, token.component_declaration.component_keyword, token.component_declaration.end_keyword)
        self.solution = 'Align :.'
