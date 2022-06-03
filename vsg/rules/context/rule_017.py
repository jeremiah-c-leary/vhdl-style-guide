
from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import context_declaration as token


class rule_017(Rule):
    '''
    This rule checks for a single space between the context identifier and the **is** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       context c1    is

    **Fix**

    .. code-block:: vhdl

       context c1 is
    '''
    def __init__(self):
        Rule.__init__(self, 'context', '017')
        self.left_token = token.identifier
        self.right_token = token.is_keyword
