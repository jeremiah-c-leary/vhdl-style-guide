
from vsg import parser

from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import case_statement as token


class rule_003(Rule):
    '''
    This rule checks for a single space before the **is** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       case data    is

    **Fix**

    .. code-block:: vhdl

       case data is
    '''
    def __init__(self):
        Rule.__init__(self, 'case', '003')
        self.left_token = parser.todo
        self.right_token = token.is_keyword
