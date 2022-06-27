
from vsg import parser

from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import case_statement as token


class rule_002(Rule):
    '''
    This rule checks for a single space after the **case** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       case    data is


    **Fix**

    .. code-block:: vhdl

       case data is
    '''
    def __init__(self):
        Rule.__init__(self, 'case', '002')
        self.left_token = token.case_keyword
        self.right_token = parser.todo
