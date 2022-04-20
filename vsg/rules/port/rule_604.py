
from vsg.rules import token_prefix as Rule

from vsg.rules import utils

from vsg import token

lTokens = []


class rule_604(Rule):
    '''
    This rule checks for valid prefixes on port identifiers for linkage ports.

    The default prefix is: *l\_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       port (
         wr_en    : linkage    std_logic;
         rd_en    : linkage    std_logic
       );


    **Fix**

    .. code-block:: vhdl

       port (
         l_wr_en    : linkage    std_logic;
         l_rd_en    : linkage    std_logic
       );
    '''

    def __init__(self):
        Rule.__init__(self, 'port', '604', lTokens)
        self.prefixes = ['l_']

    def _get_tokens_of_interest(self, oFile):
        lReturn = []
        lToi = oFile.get_interface_elements_between_tokens(token.port_clause.open_parenthesis, token.port_clause.close_parenthesis)
        lReturn = utils.extract_identifiers_with_mode_of_linkage(lToi)
        return lReturn
