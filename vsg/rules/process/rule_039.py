# -*- coding: utf-8 -*-


from vsg import token
from vsg.rules import move_token_right_to_next_non_whitespace_token as Rule

lTokens = []
lTokens.append(token.process_statement.postponed_keyword)


class rule_039(Rule):
    """
    This rule checks a **postponed** keyword is on the same line at the **process** keyword.

    **Violation**

    .. code-block:: vhdl

       label : postponed
       process

    **Fix**

    .. code-block:: vhdl

       label :
       postponed process
    """

    def __init__(self):
        super().__init__(lTokens)
