
from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import entity_declaration as token


class rule_007(Rule):
    '''
    This rule checks for a single space before the **is** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       entity fifo    is

    **Fix**

    .. code-block:: vhdl

       entity fifo is
    '''
    def __init__(self):
        Rule.__init__(self, 'entity', '007')
        self.left_token = token.identifier
        self.right_token = token.is_keyword
