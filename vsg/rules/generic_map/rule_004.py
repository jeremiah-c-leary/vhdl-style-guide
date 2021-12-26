
from vsg.rules import split_line_at_token_when_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.generic_map_aspect.close_parenthesis)

oStart = token.component_instantiation_statement.label_colon
oEnd = token.component_instantiation_statement.semicolon


class rule_004(split_line_at_token_when_between_tokens):
    '''
    This rule checks for the closing parenthesis *)* on generic maps are on their own line.

    **Violation**

    .. code-block:: vhdl

         generic map (
           GENERIC_1 => 0,
           GENERIC_2 => TRUE,
           GENERIC_3 => FALSE)

    **Fix**

    .. code-block:: vhdl

         generic map (
           GENERIC_1 => 0,
           GENERIC_2 => TRUE,
           GENERIC_3 => FALSE
         )
    '''

    def __init__(self):
        split_line_at_token_when_between_tokens.__init__(self, 'generic_map', '004', lTokens, oStart, oEnd)
        self.solution = 'Place closing ) on it\'s own line.'
