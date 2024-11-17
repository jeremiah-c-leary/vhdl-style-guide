# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.protected_type_body.end_keyword)


class rule_300(token_indent):
    """
    This rule checks the indent of the end protected type body declaration.

    **Violation**

    .. code-block:: vhdl

       type flag_pt is protected body
            end protected body;

    **Fix**

    .. code-block:: vhdl

       type flag_pt is protected body
       end protected body;
    """

    def __init__(self):
        super().__init__(lTokens)
