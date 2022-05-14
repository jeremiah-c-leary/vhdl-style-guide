
from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import context_declaration as token


class rule_018(Rule):
    '''
    This rule checks for a single space between the **end** keyword and the **context** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       end;

       end   context;

    **Fix**

    .. code-block:: vhdl

       end;

       end context;
    '''
    def __init__(self):
        Rule.__init__(self, 'context', '018')
        self.left_token = token.end_keyword
        self.right_token = token.end_context_keyword
