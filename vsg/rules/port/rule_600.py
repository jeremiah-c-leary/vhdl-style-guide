
from vsg.rules import token_prefix as Rule

from vsg import token

lTokens = []


class rule_600(Rule):
    '''
    This rule checks for valid prefixes on port identifiers for input ports.

    The default prefix is: *i\_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       port (
         wr_en    : in    std_logic;
         rd_en    : in    std_logic
       );


    **Fix**

    .. code-block:: vhdl

       port (
         i_wr_en    : in    std_logic;
         i_rd_en    : in    std_logic
       );
    '''

    def __init__(self):
        Rule.__init__(self, 'port', '600', lTokens)
        self.prefixes = ['i_']

    def _get_tokens_of_interest(self, oFile):
        lReturn = []
        lToi = oFile.get_interface_elements_between_tokens(token.port_clause.open_parenthesis, token.port_clause.close_parenthesis)
        lReturn = extract_identifiers_with_mode_of_input(lToi)
        return lReturn


def extract_identifiers_with_mode_of_input(lToi):
    lReturn = []
    for oToi in lToi:
        if interface_element_mode_is_input(oToi):
            lReturn.append(oToi.extract_tokens(0, 0))
    return lReturn


def interface_element_mode_is_input(oToi):
    lTokens = oToi.get_tokens()
    for oToken in lTokens:
        if isinstance(oToken, token.mode.in_keyword):
            return True
    return False