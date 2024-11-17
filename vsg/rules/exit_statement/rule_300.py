# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.exit_statement.exit_keyword)


class rule_300(token_indent):
    """
    This rule checks the indent of the **exit** keyword.

    **Violation**

    .. code-block:: vhdl

       end if;

         exit;

    **Fix**

    .. code-block:: vhdl

       end if;

       exit;
    """

    def __init__(self):
        super().__init__(lTokens)
