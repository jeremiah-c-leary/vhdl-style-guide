
from vsg.rules.blank_line_above_line_starting_with_token_when_between_tokens import Rule

from vsg.token import port_clause as token
from vsg.token import entity_declaration as between

lTokens = []
lTokens.append(token.port_keyword)


class rule_202(Rule):
    '''
    This rule checks for blank lines above the **port** keyword in entity specifications.

    **Violation**

    .. code-block:: vhdl

       entity fifo is



         port (

    **Fix**

    .. code-block:: vhdl

       entity fifo is
         port (
    '''
    def __init__(self):
        Rule.__init__(self, 'entity', '202', lTokens)
        self.style = 'no_blank_line'
        self.lBetweenTokenPairs = [between.entity_keyword, between.semicolon]
