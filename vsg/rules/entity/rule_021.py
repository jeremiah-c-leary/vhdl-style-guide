# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import split_line_at_token

lTokens = []
lTokens.append(token.entity_declaration.end_keyword)


class rule_021(split_line_at_token):
    """
    This rule checks the **end** keyword is on its own line.

    **Violation**

    .. code-block:: vhdl

       port (
          ...
       ); end entity;

    **Fix**

    .. code-block:: vhdl

       port (
          ...
       );
       end entity;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = "Move the **end** keyword to the next line."
