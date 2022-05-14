
from vsg import token

from vsg.rules.whitespace_after_token import Rule
from vsg.rules import utils

lTokens = []
lTokens.append(token.interface_constant_declaration.colon)
lTokens.append(token.interface_signal_declaration.colon)
lTokens.append(token.interface_variable_declaration.colon)
lTokens.append(token.interface_file_declaration.colon)
lTokens.append(token.interface_unknown_declaration.colon)

oStart = token.generic_clause.open_parenthesis
oEnd = token.generic_clause.close_parenthesis


class rule_005(Rule):
    '''
    This rule checks for a single space after the colon in a generic declaration.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       g_width :integer := 32;

    **Fix**

    .. code-block:: vhdl

       g_width : integer := 32;
    '''
    def __init__(self):
        Rule.__init__(self, 'generic', '005', lTokens)
        self.solution = 'Reduce number of spaces after the colon to 1.'

    def _get_tokens_of_interest(self, oFile):
        lToi = oFile.get_token_and_n_tokens_after_it_when_between_tokens(self.lTokens, 2, oStart, oEnd)
        lToi = utils.remove_toi_if_token_is_at_the_end_of_the_line(lToi)
        return lToi
