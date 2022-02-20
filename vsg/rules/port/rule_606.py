
from vsg.rules import token_suffix as Rule

from vsg.rules import utils

from vsg import token

lTokens = []


class rule_606(Rule):
    '''
    This rule checks for valid suffixes on port identifiers for output ports.

    The default suffix is: *_o*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       port (
         wr_en    : out    std_logic;
         rd_en    : out    std_logic
       );

    **Fix**

    .. code-block:: vhdl

       port (
         wr_en_o    : out    std_logic;
         rd_en_o    : out    std_logic
       );
    '''

    def __init__(self):
        Rule.__init__(self, 'port', '606', lTokens)
        self.suffixes = ['_o']

    def _get_tokens_of_interest(self, oFile):
        lReturn = []
        lToi = oFile.get_interface_elements_between_tokens(token.port_clause.open_parenthesis, token.port_clause.close_parenthesis)
        lReturn = utils.extract_identifiers_with_mode_of_out(lToi)
        return lReturn
