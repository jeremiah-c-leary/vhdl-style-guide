
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment as Rule

from vsg.token import entity_declaration as token

lTokens = []
lTokens.append(token.begin_keyword)


class rule_027(Rule):
    '''
    This rule checks for code after the **begin** keyword.

    **Violation**

    .. code-block:: vhdl

       begin end entity;

    **Fix**

    .. code-block:: vhdl

        begin
        end entity;
    '''

    def __init__(self):
        Rule.__init__(self, 'entity', '027', lTokens)
        self.solution = 'Move code after the **begin** keyword to the next line.'
