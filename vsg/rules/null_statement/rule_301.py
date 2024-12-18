# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent as Rule

lTokens = []
lTokens.append(token.null_statement.label)


class rule_301(Rule):
    """
    This rule checks the indentation of the label.

    **Violation**

    .. code-block:: vhdl

         null_label : null;
         end loop;

    **Fix**

    .. code-block:: vhdl

           null_label : null;
         end loop;
    """

    def __init__(self):
        super().__init__(lTokens)
