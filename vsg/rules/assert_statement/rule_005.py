
from vsg.rules import split_line_at_token_when_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.assertion.severity_keyword)

oStart = token.assertion.keyword
oEnd = token.assertion_statement.semicolon


class rule_005(split_line_at_token_when_between_tokens):
    '''
    Checks the severity keyword is on it's own line for assertion statements.
    '''

    def __init__(self):
        split_line_at_token_when_between_tokens.__init__(self, 'assert', '005', lTokens, oStart, oEnd)
        self.solution = "Place **severity** keyword on it's own line."
