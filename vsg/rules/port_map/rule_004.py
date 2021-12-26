
from vsg.rules import split_line_at_token_when_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.port_map_aspect.close_parenthesis)

oStart = token.component_instantiation_statement.label_colon
oEnd = token.component_instantiation_statement.semicolon


class rule_004(split_line_at_token_when_between_tokens):
    '''
    This rule checks the closing ")" character for the port map is on it's own line.

    **Violation**

    .. code-block:: vhdl

        port map (
          WR_EN => wr_en);

    **Fix**

    .. code-block:: vhdl

        port map (
          WR_EN => wr_en
        );
    '''

    def __init__(self):
        split_line_at_token_when_between_tokens.__init__(self, 'port_map', '004', lTokens, oStart, oEnd)
        self.solution = 'Place closing ); on it\'s own line.'
