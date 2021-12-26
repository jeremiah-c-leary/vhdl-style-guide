
from vsg.rules import split_line_at_token_when_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.generic_map_aspect.generic_keyword)

oStart = token.component_instantiation_statement.label_colon
oEnd = token.component_instantiation_statement.semicolon


class rule_012(split_line_at_token_when_between_tokens):
    '''
    This rule checks the instantiation declaration and the **generic map** keywords are not on the same line.

    **Violation**

    .. code-block:: vhdl

       U_FIFO : FIFO generic map (

    **Fix**

    .. code-block:: vhdl

       U_FIFO : FIFO
         generic map (
    '''

    def __init__(self):
        split_line_at_token_when_between_tokens.__init__(self, 'instantiation', '012', lTokens, oStart, oEnd)
        self.solution = 'Place *generic map* keywords on the next line by itself'
