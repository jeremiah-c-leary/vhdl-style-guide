# -*- coding: utf-8 -*-

from vsg.rules import move_token_next_to_another_token
from vsg.token import package_instantiation_declaration as token


class rule_003(move_token_next_to_another_token):
    """
    This rule checks the **new** keyword is on the same line as the **is** keyword.

    **Violation**

    .. code-block:: vhdl

       package my_pkg is
       new my_generic_pkg

    **Fix**

    .. code-block:: vhdl

       package my_pkg is new my_generic_pkg
    """

    def __init__(self):
        super().__init__(token.is_keyword, token.new_keyword)
        self.solution = "Ensure the *new* keyword is on the same line as the *is* keyword."
