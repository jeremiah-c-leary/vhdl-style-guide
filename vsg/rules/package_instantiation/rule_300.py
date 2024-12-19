# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.package_instantiation_declaration.package_keyword)


class rule_300(token_indent):
    """
    This rule checks the indent of the package declaration.

    **Violation**

    .. code-block:: vhdl

       library ieee;

         package my_pkg is new my_generic_pkg

    **Fix**

    .. code-block:: vhdl

       library ieee;

       package my_pkg is new my_generic_pkg
    """

    def __init__(self):
        super().__init__(lTokens)
