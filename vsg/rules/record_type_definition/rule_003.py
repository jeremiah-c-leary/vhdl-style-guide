
from vsg.rules import split_line_at_token as Rule

from vsg import token

lTokens = []
lTokens.append(token.record_type_definition.end_keyword)


class rule_003(Rule):
    '''
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
    '''

    def __init__(self):
        Rule.__init__(self, 'record_type_definition', '003', lTokens)
        self.solution = 'Move *end* keyword and code after it to the next line'
