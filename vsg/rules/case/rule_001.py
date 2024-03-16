# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.case_statement.case_keyword)
lTokens.append(token.case_statement.end_keyword)
lTokens.append(token.case_statement_alternative.when_keyword)


class rule_001(token_indent):
    """
    This rule checks the indent of **case**, **when**, and **end case** keywords.

    **Violation**

    .. code-block:: vhdl


       case data is

           when 0 =>
       when 1 =>
               when 3 =>

      end case;

    **Fix**

    .. code-block:: vhdl

      case data is

        when 0 =>
        when 1 =>
        when 3 =>

      end case;
    """

    def __init__(self):
        super().__init__(lTokens)
