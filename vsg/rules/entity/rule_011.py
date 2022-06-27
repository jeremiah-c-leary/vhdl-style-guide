
from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import entity_declaration as token


class rule_011(Rule):
    '''
    This rule checks for a single space after the **end** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       end    entity fifo;

    **Fix**

    .. code-block:: vhdl

       end entity fifo;
    '''
    def __init__(self):
        Rule.__init__(self, 'entity', '011')
        self.left_token = token.end_keyword
        self.right_token = token.end_entity_keyword
