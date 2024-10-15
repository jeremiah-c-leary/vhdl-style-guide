# -*- coding: utf-8 -*-


from vsg.rules import move_token_next_to_another_token as Rule
from vsg.token import subtype_declaration as token


class rule_005(Rule):
    """
    This rule checks the identifier is on the same line as the **subtype** keyword.

    **Violation**

    .. code-block:: vhdl

       subtype
       st_counter is

    **Fix**

    .. code-block:: vhdl

       subtype st_counter
       is
    """

    def __init__(self):
        super().__init__(token.subtype_keyword, token.identifier)
        self.solution = "Ensure identifier is on the same line as the *subtype* keyword."
