# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import move_token_next_to_another_token


class rule_003(move_token_next_to_another_token):
    """
    This rule checks the **is** keyword is on the same line as the new subprogram identifier.

    **Violation**

    .. code-block:: vhdl

       procedure my_proc
       is new my_generic_proc

    **Fix**

    .. code-block:: vhdl

       procedure my_proc is new my_generic_proc
    """

    def __init__(self):
        super().__init__(token.subprogram_instantiation_declaration.identifier, token.subprogram_instantiation_declaration.is_keyword)
        self.solution = "Ensure the *is* keyword is on the same line as the new subprogram identifier."
