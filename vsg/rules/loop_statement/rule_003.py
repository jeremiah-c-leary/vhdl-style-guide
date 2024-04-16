# -*- coding: utf-8 -*-


from vsg.rules import move_token_next_to_another_token
from vsg.token import loop_statement as token


class rule_003(move_token_next_to_another_token):
    """
    This rule checks the **end** keyword is on the same line as the **end loop** keyword.

    **Violation**

    .. code-block:: vhdl

       end
       loop;

    **Fix**

    .. code-block:: vhdl

       end loop;
    """

    def __init__(self):
        super().__init__(token.end_keyword, token.end_loop_keyword)
        self.solution = "Ensure *end* keyword is on the same line as the *loop* keyword."
