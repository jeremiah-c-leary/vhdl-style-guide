
from vsg.rules import move_token_next_to_another_token_if_it_exists_between_tokens

from vsg.token import context_declaration as token

lBetweenTokens = [token.end_keyword, token.semicolon]


class rule_009(move_token_next_to_another_token_if_it_exists_between_tokens):
    '''
    This rule checks the **context** keyword is on the same line as the end context keyword.

    **Violation**

    .. code-block:: vhdl

       end
       context c1;

    **Fix**

    .. code-block:: vhdl

       end context
         c1;
    '''

    def __init__(self):
        move_token_next_to_another_token_if_it_exists_between_tokens.__init__(self, 'context', '009', token.end_keyword, token.end_context_keyword, lBetweenTokens)
        self.subphase = 1
        self.solution = 'Move identifier next to *end* keyword'
