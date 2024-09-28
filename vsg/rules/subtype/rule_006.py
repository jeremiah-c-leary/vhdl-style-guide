# -*- coding: utf-8 -*-


from vsg.rules import move_token_next_to_another_token as Rule
from vsg.token import subtype_declaration as token


class rule_006(Rule):
    """
    This rule checks the **is** keyword is on the same line as the identifier.

    **Violation**

    .. code-block:: vhdl

       subtype st_counter
       is

    **Fix**

    .. code-block:: vhdl

       subtype st_counter is
    """

    def __init__(self):
        super().__init__(token.identifier, token.is_keyword)
        self.solution = "Ensure *is* keyword is on the same line as the identifier."
        self.subphase = 2
