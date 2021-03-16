
from vsg.rules import split_line_at_token

from vsg import token

lTokens = []
lTokens.append(token.context_declaration.end_keyword)


class rule_008(split_line_at_token):
    '''
    Moves context end keyword and code following it to the next line
    '''

    def __init__(self):
        split_line_at_token.__init__(self, 'context', '008', lTokens)
        self.solution = 'Move *end* keyword and code after end to the next line'
