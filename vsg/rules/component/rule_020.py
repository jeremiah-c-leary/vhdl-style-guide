
from vsg.rules import align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens

from vsg import parser
from vsg import token

lAlign = []
lAlign.append(parser.comment)

lSkip = []
lSkip.append(parser.comment)


class rule_020(align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens):
    '''
    This rule checks for alignment of inline comments in the component declaration.

    Following extra configurations are supported:

    * :code:`separate_generic_port_alignment`.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       component my_component
           generic (
               g_width        : positive;  -- Data width
               g_output_delay : positive -- Delay at output
           );
           port (
               clk_i  : in std_logic; -- Input clock
               data_i : in std_logic;   -- Data input
               data_o : in std_logic -- Data output
           );
       end my_component;

    **Fix**

    .. code-block:: vhdl

       component my_component
           generic (
               g_width        : positive; -- Data width
               g_output_delay : positive  -- Delay at output
           );
           port (
               clk_i  : in std_logic; -- Input clock
               data_i : in std_logic; -- Data input
               data_o : in std_logic  -- Data output
           );
       end my_component;
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens.__init__(self, 'component', '020', lAlign, token.component_declaration.component_keyword, token.component_declaration.end_keyword, lSkip)
        self.solution = 'Align identifer.'
        self.subphase = 2
