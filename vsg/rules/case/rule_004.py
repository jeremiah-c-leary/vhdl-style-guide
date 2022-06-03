
from vsg import parser

from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import case_statement_alternative as token


class rule_004(Rule):
    '''
    This rule checks for a single space after the **when** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

      case data is

        when   3 =>

    **Fix**

    .. code-block:: vhdl

      case data is

        when 3 =>
    '''
    def __init__(self):
        Rule.__init__(self, 'case', '004')
        self.left_token = token.when_keyword
        self.right_token = parser.todo
