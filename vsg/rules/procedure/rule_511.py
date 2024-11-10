# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_in_range_bounded_by_tokens

lTokens = []
lTokens.append(token.interface_variable_declaration.variable_keyword)
lTokens.append(token.interface_constant_declaration.constant_keyword)
lTokens.append(token.interface_signal_declaration.signal_keyword)
lTokens.append(token.interface_file_declaration.file_keyword)

oStart = token.procedure_specification.open_parenthesis
oEnd = token.procedure_specification.close_parenthesis


class rule_511(token_case_in_range_bounded_by_tokens):
    """
    This rule checks the parameter class has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

      procedure my_func (
        a          : integer;
        VARIABLE b : integer;
        CONSTANT c : integer;
        SIGNAL   d : integer;
        FILE     e : file_type
      );

    **Fix**

    .. code-block:: vhdl

      procedure my_func (
        a          : integer;
        variable b : integer;
        constant c : integer;
        signal   d : integer;
        file     e : file_type
      );
    """

    def __init__(self):
        super().__init__(lTokens, oStart, oEnd)
        self.groups.append("case::keyword")
