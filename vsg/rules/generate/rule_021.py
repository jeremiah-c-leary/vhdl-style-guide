# -*- coding: utf-8 -*-


from vsg import token
from vsg.rules import move_token_right_to_next_non_whitespace_token as Rule

lTokens = []
lTokens.append(token.case_generate_statement.label_colon)
lTokens.append(token.for_generate_statement.label_colon)
lTokens.append(token.if_generate_statement.label_colon)


class rule_021(Rule):
    """
    This rule checks a label colon is on the same line as the **case**, **if**, and **for** keywords.

    **Violation**

    .. code-block:: vhdl

       label :
       case

    **Fix**

    .. code-block:: vhdl

       label
       : case
    """

    def __init__(self):
        super().__init__(lTokens)
        self.subphase = 2
