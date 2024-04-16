# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import (
    move_token_to_the_right_of_several_possible_tokens_if_it_exists_between_tokens,
)

lAnchorTokens = []
lAnchorTokens.append(token.context_declaration.end_keyword)
lAnchorTokens.append(token.context_declaration.end_context_keyword)
lAnchorTokens.append(token.context_declaration.context_simple_name)

oToken = token.context_declaration.semicolon

oStartToken = token.context_declaration.end_keyword
oEndToken = token.context_declaration.semicolon


class rule_011(move_token_to_the_right_of_several_possible_tokens_if_it_exists_between_tokens):
    """
    This rule checks the semicolon is on the same line as the **end** keyword.

    **Violation**

    .. code-block:: vhdl

       end
       ;

       end context
       ;

       end context c1
       ;


    **Fix**

    .. code-block:: vhdl

       end;

       end context;

       end context c1;
    """

    def __init__(self):
        super().__init__(oToken, lAnchorTokens, oStartToken, oEndToken)
        self.subphase = 3
