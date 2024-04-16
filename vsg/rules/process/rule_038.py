# -*- coding: utf-8 -*-


from vsg import token
from vsg.rules import move_token_right_to_next_non_whitespace_token as Rule

lTokens = []
lTokens.append(token.process_statement.label_colon)


class rule_038(Rule):
    """
    This rule checks a label colon is on the same line as the **process** or **postponed** keyword.

    **Violation**

    .. code-block:: vhdl

       label :
       process

    **Fix**

    .. code-block:: vhdl

       label
       : process
    """

    def __init__(self):
        super().__init__(lTokens)
        self.subphase = 2
