
from vsg.rules import move_token_to_the_right_of_several_possible_tokens_if_it_exists_between_tokens

from vsg.token import block_statement as token

lAnchorTokens = []
lAnchorTokens.append(token.block_keyword)
lAnchorTokens.append(token.guard_close_parenthesis)

oToken = token.is_keyword

oStartToken = token.block_keyword
oEndToken = token.begin_keyword


class rule_003(move_token_to_the_right_of_several_possible_tokens_if_it_exists_between_tokens):
    '''
    This rule checks the **is** keyword is on the same line as the **block** keyword.

    **Violation**

    .. code-block:: vhdl

       block_label : block
       is

    **Fix**

    .. code-block:: vhdl

       block_labeel : block is
    '''

    def __init__(self):
        move_token_to_the_right_of_several_possible_tokens_if_it_exists_between_tokens.__init__(self, 'block', '003', oToken, lAnchorTokens, oStartToken, oEndToken, bInsertWhitespace=True)
        self.solution = 'Move block_simple_name next to *block* keyword'
