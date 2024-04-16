# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.variable_assignment_statement.label)
lTokens.append(token.simple_variable_assignment.simple_name)
lTokens.append(token.simple_variable_assignment.aggregate_open_parenthesis)
lTokens.append(token.simple_variable_assignment.aggregate_close_parenthesis)
lTokens.append(token.conditional_variable_assignment.target)
lTokens.append(token.selected_variable_assignment.with_keyword)


class rule_001(token_indent):
    """
    This rule checks the indent of a variable assignment.

    **Violation**

    .. code-block:: vhdl

       proc : process () is
       begin

           counter := 0;
       count := counter + 1;


    **Fix**

    .. code-block:: vhdl

       proc : process () is
       begin

         counter := 0;
         count   := counter + 1;

    """

    def __init__(self):
        super().__init__(lTokens)
