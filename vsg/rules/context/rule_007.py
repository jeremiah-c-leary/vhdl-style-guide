# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import split_line_at_token

lTokens = []
lTokens.append(token.library_clause.keyword)


class rule_007(split_line_at_token):
    """
    This rule checks for code after the **is** keyword.

    **Violation**

    .. code-block:: vhdl

       context c1 is -- Comments are allowed

       context c1 is library ieee; -- This is not allowed

    **Fix**

    .. code-block:: vhdl

       context c1 is -- Comments are allowed

       context c1 is
         library ieee; -- This is not allowed
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = "Move library and code after library to the next line"
