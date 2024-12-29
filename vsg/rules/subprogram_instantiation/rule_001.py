# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import move_token_next_to_another_token


class rule_001(move_token_next_to_another_token):
    """
    This rule checks the new **procedure** keyword is on the same line as the new subprogram identifier.

    **Violation**

    .. code-block:: vhdl

       procedure
       my_proc is new my_generic_proc

    **Fix**

    .. code-block:: vhdl

       procedure my_proc is new my_generic_proc
    """

    def __init__(self):
        super().__init__(token.subprogram_kind.procedure_keyword, token.subprogram_instantiation_declaration.identifier)
        self.solution = "Ensure the *procedure* keyword is on the same line as the new package identifier."
