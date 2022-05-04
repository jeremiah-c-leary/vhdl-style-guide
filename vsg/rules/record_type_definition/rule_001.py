
from vsg.rules import move_token as Rule

from vsg import token

oToken = token.record_type_definition.record_keyword


class rule_001(Rule):
    '''
    This rule checks the location of the **record** keyword.

    The default location is not on a line by itself.

    |configuring_move_token_rules_link|

    **Violation**

    .. code-block:: vhdl

       type t_record is
       record

    **Fix**

    .. code-block:: vhdl

       type t_record is record
    '''

    def __init__(self):
        Rule.__init__(self, 'record_type_definition', '001', oToken)
        self.action = 'same_line'
        self.subphase = 3
        self.insert_whitespace = True
