
from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import architecture_body as token


class rule_012(Rule):
    '''
    This rule checks for a single space between **end** and **architecture** keywords.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       end    architecture architecture_name;

    **Fix**

    .. code-block:: vhdl

       end architecture architecture_name;
    '''
    def __init__(self):
        Rule.__init__(self, 'architecture', '012')
        self.left_token = token.end_keyword
        self.right_token = token.end_architecture_keyword
