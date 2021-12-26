
from vsg import parser
from vsg import token

from vsg.rules import consistent_case_of_tokens_from_between_tokens_applied_to_region

lTokens = []
lTokens.append(token.interface_unknown_declaration.identifier)
lTokens.append(token.interface_constant_declaration.identifier)
lTokens.append(token.interface_variable_declaration.identifier)
lTokens.append(token.interface_signal_declaration.identifier)

lIgnore = []
lIgnore.append(parser.whitespace)
lIgnore.append(parser.carriage_return)
lIgnore.append(parser.blank_line)
lIgnore.append(token.identifier.identifier)

oStartToken = token.generic_clause.open_parenthesis
oEndToken = token.generic_clause.close_parenthesis

oRegionStart = token.port_clause.open_parenthesis
oRegionEnd = token.port_clause.close_parenthesis


class rule_600(consistent_case_of_tokens_from_between_tokens_applied_to_region):
    '''
    This rule checks for consistent capitalization of generic names in entity declarations.

    **Violation**

    .. code-block:: vhdl

       entity FIFO is
         generic (
           G_WIDTH : natural := 16
         );
         port (
           I_DATA : std_logic_vector(g_width - 1 downto 0);
           O_DATA : std_logic_vector(g_width - 1 downto 0)
         );
       end entity fifo;

    **Fix**

    .. code-block:: vhdl

       entity FIFO is
         generic (
           G_WIDTH : natural := 16
         );
         port (
           I_DATA : std_logic_vector(G_WIDTH - 1 downto 0);
           O_DATA : std_logic_vector(G_WIDTH - 1 downto 0)
         );
       end entity fifo;
    '''

    def __init__(self):
        consistent_case_of_tokens_from_between_tokens_applied_to_region.__init__(self, 'entity', '600', lTokens, oStartToken, oEndToken, oRegionStart, oRegionEnd, lIgnore)
