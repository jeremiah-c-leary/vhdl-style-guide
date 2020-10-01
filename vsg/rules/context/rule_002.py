
from vsg.rules import single_space_between_tokens

from vsg.token import context_declaration as token


class rule_002(single_space_between_tokens):
    '''
    Checks for a single space between the context keyword and the context identifier
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'context', '002', token.context_keyword, token.identifier)
        self.solution = 'Reduce spaces between *context* keyword and identifier.'
