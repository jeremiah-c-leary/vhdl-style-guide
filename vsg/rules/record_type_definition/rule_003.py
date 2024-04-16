# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import split_line_at_token as Rule

lTokens = []
lTokens.append(token.record_type_definition.end_keyword)


class rule_003(Rule):
    """
    This rule checks the **end** keyword is on its own line.

    **Violation**

    .. code-block:: vhdl

       type t_record is record
         a : std_logic;
         b : std_logic; end record;


    **Fix**

    .. code-block:: vhdl

       type t_record is record
         a : std_logic;
         b : std_logic;
       end record;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = "Move *end* keyword and code after it to the next line"
