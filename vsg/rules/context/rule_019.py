
from vsg.rules import single_space_between_tokens

from vsg.token import context_declaration as token


class rule_019(single_space_between_tokens):
    '''
    Checks for a single space between the context keyword and the context identifier in the end context portion of a context declaration.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'context', '019', token.end_context_keyword, token.context_simple_name)
        self.solution = 'Reduce spaces between *context* keyword and context_simple_name to a single space.'
