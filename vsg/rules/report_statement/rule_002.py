
from vsg.rules import split_line_at_token_when_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.report_statement.severity_keyword)

oStart = token.report_statement.report_keyword
oEnd = token.report_statement.semicolon


class rule_002(split_line_at_token_when_between_tokens):
    '''
    Checks the severity keyword is on it's own line for report_statement statements.
    '''

    def __init__(self):
        split_line_at_token_when_between_tokens.__init__(self, 'report_statement', '002', lTokens, oStart, oEnd)
        self.solution = "Place **severity** keyword on it's own line."
