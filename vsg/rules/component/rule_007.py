
from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import component_declaration as token


class rule_007(Rule):
    '''
    This rule checks for a single space before the **is** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       component fifo    is

    **Fix**

    .. code-block:: vhdl

       component fifo is
    '''
    def __init__(self):
        Rule.__init__(self, 'component', '007')
        self.left_token = token.identifier
        self.right_token = token.is_keyword
