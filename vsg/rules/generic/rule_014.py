
from vsg import token

from vsg.rules.whitespace_before_tokens_in_between_tokens import Rule

lTokens = []
lTokens.append(token.interface_constant_declaration.colon)
lTokens.append(token.interface_signal_declaration.colon)
lTokens.append(token.interface_variable_declaration.colon)
lTokens.append(token.interface_file_declaration.colon)
lTokens.append(token.interface_unknown_declaration.colon)

oStart = token.generic_clause.open_parenthesis
oEnd = token.generic_clause.close_parenthesis


class rule_014(Rule):
    '''
    This rule checks for at least a single space before the colon.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       g_address_width: integer := 10;
       g_data_width : integer := 32;
       g_depth: integer := 512;

    **Fix**

    .. code-block:: vhdl

       g_address_width : integer := 10;
       g_data_width : integer := 32;
       g_depth : integer := 512;
    '''
    def __init__(self):
        Rule.__init__(self, 'generic', '014', lTokens, oStart, oEnd)
        self.number_of_spaces = '>=1'
