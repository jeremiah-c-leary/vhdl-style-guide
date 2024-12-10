# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import move_token_next_to_another_token


class rule_002(move_token_next_to_another_token):
    """
    This rule checks the **is** keyword is on the same line as the new package identifier.

    **Violation**

    .. code-block:: vhdl

       package my_pkg
       is new my_generic_pkg

    **Fix**

    .. code-block:: vhdl

       package my_pkg is new my_generic_pkg
    """

    def __init__(self):
        super().__init__(token.identifier.identifier, token.package_instantiation_declaration.is_keyword)
        self.solution = "Ensure the *is* keyword is on the same line as the new package identifier."
