# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.exit_statement.label)


class rule_301(token_indent):
    """
    This rule checks the indent of the label.

    **Violation**

    .. code-block:: vhdl

       end if;

         exit_label : exit;

    **Fix**

    .. code-block:: vhdl

       end if;

       exit_label : exit;
    """

    def __init__(self):
        super().__init__(lTokens)
