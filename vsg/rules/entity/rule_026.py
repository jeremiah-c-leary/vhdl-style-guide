
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment as Rule

from vsg.token import entity_declaration as token

lTokens = []
lTokens.append(token.is_keyword)


class rule_026(Rule):
    '''
    This rule checks for code after the **is** keyword.

    **Violation**

    .. code-block:: vhdl

       entity FIFO is port (

    **Fix**

    .. code-block:: vhdl

       entity FIFO is
         port (
    '''

    def __init__(self):
        Rule.__init__(self, 'entity', '026', lTokens)
        self.solution = 'Move code after the **is** keyword to the next line.'
