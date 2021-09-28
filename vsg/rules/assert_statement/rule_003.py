
from vsg.rules import split_line_at_token_when_between_tokens_unless_token_is_found

from vsg import token

lTokens = []
lTokens.append(token.assertion.report_keyword)

oStart = token.assertion.keyword
oEnd = token.assertion_statement.semicolon
oStop = token.concurrent_assertion_statement.semicolon


class rule_003(split_line_at_token_when_between_tokens_unless_token_is_found):
    '''
    Checks the report keyword is on its own line for assertion statements.
    '''

    def __init__(self):
        split_line_at_token_when_between_tokens_unless_token_is_found.__init__(self, 'assert', '003', lTokens, oStart, oEnd, oStop)
        self.solution = "Place **report** keyword on its own line."
