
from vsg import parser

from vsg.rules import remove_spaces_before_token_rule


class rule_006(remove_spaces_before_token_rule):
    '''
    This rule checks for spaces before a close parenthesis.

    **Violation**

    .. code-block:: vhdl

       signal data        : std_logic_vector(31 downto 0    );
       signal byte_enable : std_logic_vector( 3 downto 0 );
       signal width       : std_logic_vector(g_width - 1 downto 0);

    **Fix**

    .. code-block:: vhdl

       signal data        : std_logic_vector(31 downto 0);
       signal byte_enable : std_logic_vector( 3 downto 0);
       signal width       : std_logic_vector(g_width - 1 downto 0);
    '''

    def __init__(self):
        remove_spaces_before_token_rule.__init__(self, 'whitespace', '006', parser.close_parenthesis, bIgnoreIfLineStart=True)
        self.solution = 'Remove spaces before close ).'
