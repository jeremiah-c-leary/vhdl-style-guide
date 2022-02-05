
from vsg.rules import move_token_to_the_right_of_several_possible_tokens_if_it_exists_between_tokens as Rule

from vsg import token

lAnchorTokens = []
lAnchorTokens.append(token.loop_statement.end_loop_keyword)
lAnchorTokens.append(token.loop_statement.end_loop_label)

oToken = token.loop_statement.semicolon

oStartToken = token.loop_statement.end_loop_keyword
oEndToken = token.loop_statement.semicolon


class rule_004(Rule):
    '''
    This rule checks the semicolon is on the same line as the **end loop** keyword.

    **Violation**

    .. code-block:: vhdl

       end loop
       ;

       end loop LOOP_LABEL
       ;

    **Fix**

    .. code-block:: vhdl

       end loop;

       end loop LOOP_LABEL;
    '''

    def __init__(self):
        Rule.__init__(self, 'loop_statement', '004', oToken, lAnchorTokens, oStartToken, oEndToken)
        self.subphase = 3
