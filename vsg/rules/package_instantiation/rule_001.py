# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import move_token_next_to_another_token


class rule_001(move_token_next_to_another_token):
    """
    This rule checks the new package identifier is on the same line as the **package** keyword.

    **Violation**

    .. code-block:: vhdl

       package
       my_pkg is new my_generic_pkg

    **Fix**

    .. code-block:: vhdl

       package my_pkg is new my_generic_pkg
    """

    def __init__(self):
        super().__init__(token.package_instantiation_declaration.package_keyword, token.identifier.identifier)
        self.solution = "Ensure the new package identifier is on the same line as the *package* keyword."
