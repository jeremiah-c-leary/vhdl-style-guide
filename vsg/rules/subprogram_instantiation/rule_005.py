# -*- coding: utf-8 -*-

from vsg.rules import move_token_next_to_another_token
from vsg.token import subprogram_instantiation_declaration as token


class rule_005(move_token_next_to_another_token):
    """
    This rule checks the uninstantiated subprogram name is on the same line as the **new** keyword.

    **Violation**

    .. code-block:: vhdl

       procedure my_proc is new
       my_generic_proc

    **Fix**

    .. code-block:: vhdl

       procedure my_proc is new my_generic_proc
    """

    def __init__(self):
        super().__init__(token.new_keyword, token.uninstantiated_subprogram_name)
        self.solution = "Ensure the uninstantiated subprogram name is on the same line as the *new* keyword."
