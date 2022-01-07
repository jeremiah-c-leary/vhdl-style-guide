
from vsg.rules.blank_line_above_line_starting_with_token_when_between_tokens import Rule

from vsg.token import generic_clause as token
from vsg.token import entity_declaration as between

lTokens = []
lTokens.append(token.generic_keyword)


class rule_200(Rule):
    '''
    This rule checks for blank lines above the **generic** keyword in entity specifications.

    **Violation**

    .. code-block:: vhdl

       entity fifo is



         generic (

    **Fix**

    .. code-block:: vhdl

       entity fifo is
         generic (
    '''
    def __init__(self):
        Rule.__init__(self, 'entity', '200', lTokens)
        self.style = 'no_blank_line'
        self.lBetweenTokenPairs = [between.entity_keyword, between.semicolon]
