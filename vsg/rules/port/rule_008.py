
from vsg import token

from vsg.rules import n_spaces_between_token_pairs_when_bounded_by_tokens

lTokens = []
lTokens.append([token.mode.out_keyword, token.interface_unknown_declaration.subtype_indication])
lTokens.append([token.mode.out_keyword, token.interface_signal_declaration.subtype_indication])
lTokens.append([token.mode.out_keyword, token.interface_constant_declaration.subtype_indication])
lTokens.append([token.mode.out_keyword, token.interface_variable_declaration.subtype_indication])

oStart = token.port_clause.open_parenthesis
oEnd = token.port_clause.close_parenthesis


class rule_008(n_spaces_between_token_pairs_when_bounded_by_tokens):
    '''
    This rule checks for three spaces after the **out** keyword.
    
    **Violation**
    
    .. code-block:: vhdl
    
       port (
         WR_EN    : in    std_logic;
         RD_EN    : in    std_logic;
         OVERFLOW : out std_logic
       );
    
    
    **Fix**
    
    .. code-block:: vhdl
    
       port (
         WR_EN    : in    std_logic;
         RD_EN    : in    std_logic;
         OVERFLOW : out   std_logic
       );
    '''
    def __init__(self):
        n_spaces_between_token_pairs_when_bounded_by_tokens.__init__(self, 'port', '008', 3, lTokens, oStart, oEnd)
        self.solution = 'Change the number of spaces after the *out* keyword to three spaces.'
