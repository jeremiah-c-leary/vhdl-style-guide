# -*- coding: utf-8 -*-

from vsg.rules import blank_line_below_line_ending_with_token
from vsg.token import package_instantiation_declaration as token

lTokens = []
lTokens.append(token.uninstantiated_package_name)


class rule_201(blank_line_below_line_ending_with_token):
    """
    This rule checks for blank lines below the package instantiation.

    |configuring_blank_lines_link|

    The default style is :code:`no_blank_line`.

    **Violation**

    .. code-block:: vhdl

       package my_pkg is new my_generic_pkg

         generic map (

    **Fix**

    .. code-block:: vhdl

       package my_pkg is new my_generic_pkg
         generic map (
    """

    def __init__(self):
        super().__init__(lTokens)
        self.style = "no_blank_line"
