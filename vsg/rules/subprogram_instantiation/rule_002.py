# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import move_token_next_to_another_token


class rule_002(move_token_next_to_another_token):
    """
    This rule checks the new subprogram identifier is on the same line as the **function** keyword.

    **Violation**

    .. code-block:: vhdl

       function
       my_func is new my_generic_func

    **Fix**

    .. code-block:: vhdl

       function my_func is new my_generic_func
    """

    def __init__(self):
        super().__init__(token.subprogram_kind.function_keyword, token.subprogram_instantiation_declaration.identifier)
        self.solution = "Ensure the *function* keyword is on the same line as the new package identifier."
