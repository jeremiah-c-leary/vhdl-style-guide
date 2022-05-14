
from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import entity_declaration as token


class rule_013(Rule):
    '''
    This rule checks for a single space after the **entity** keyword in the closing of the entity declaration.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       end entity    fifo;

    **Fix**

    .. code-block:: vhdl

       end entity fifo;
    '''
    def __init__(self):
        Rule.__init__(self, 'entity', '013')
        self.left_token = token.end_entity_keyword
        self.right_token = token.entity_simple_name
