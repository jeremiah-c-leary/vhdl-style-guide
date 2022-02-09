
from vsg import token

from vsg.rules import number_of_lines_between_tokens

oLeftToken = token.process_statement.process_keyword
oRightToken = token.process_statement.semicolon

iLines = 500


class rule_003(number_of_lines_between_tokens):
    '''
    This rule checks the length of a process statement.

    |configuring_length_rules_link|
    '''

    def __init__(self):
        number_of_lines_between_tokens.__init__(self, 'length', '003', oLeftToken, oRightToken, iLines)
