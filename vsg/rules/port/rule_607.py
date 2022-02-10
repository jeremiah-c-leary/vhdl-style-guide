
from vsg.rules import token_suffix as Rule

from vsg.rules import utils

from vsg import token

lTokens = []


class rule_607(Rule):
    '''
    This rule checks for valid suffixes on port identifiers for inout ports.

    The default suffix is: *_io*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       port (
         wr_en    : inout    std_logic;
         rd_en    : inout    std_logic
       );

    **Fix**

    .. code-block:: vhdl

       port (
         wr_en_io    : inout    std_logic;
         rd_en_io    : inout    std_logic
       );
    '''

    def __init__(self):
        Rule.__init__(self, 'port', '607', lTokens)
        self.suffixes = ['_io']

    def _get_tokens_of_interest(self, oFile):
        lReturn = []
        lToi = oFile.get_interface_elements_between_tokens(token.port_clause.open_parenthesis, token.port_clause.close_parenthesis)
        lReturn = utils.extract_identifiers_with_mode_of_inout(lToi)
        return lReturn
