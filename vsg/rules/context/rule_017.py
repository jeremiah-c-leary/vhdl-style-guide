
from vsg.rules import single_space_between_tokens

from vsg.token import context_declaration as token


class rule_017(single_space_between_tokens):
    '''
    Checks for a single space between the context identifier and the is keyword
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'context', '017', token.identifier, token.is_keyword)
        self.solution = 'Reduce spaces between identifier and *is* keyword to a single space.'
