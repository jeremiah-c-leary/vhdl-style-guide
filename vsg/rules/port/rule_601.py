
from vsg.rules import token_prefix as Rule

from vsg.rules import utils

from vsg import token

lTokens = []


class rule_601(Rule):
    '''
    This rule checks for valid prefixes on port identifiers for output ports.

    The default prefix is: *o\_*.

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
         o_wr_en    : out    std_logic;
         o_rd_en    : out    std_logic
       );
    '''

    def __init__(self):
        Rule.__init__(self, 'port', '601', lTokens)
        self.prefixes = ['o_']

    def _get_tokens_of_interest(self, oFile):
        lReturn = []
        lToi = oFile.get_interface_elements_between_tokens(token.port_clause.open_parenthesis, token.port_clause.close_parenthesis)
        lReturn = utils.extract_identifiers_with_mode_of_out(lToi)
        return lReturn
