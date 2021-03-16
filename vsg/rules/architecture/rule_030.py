
from vsg.rules import single_space_between_tokens

from vsg.token import architecture_body as token

class rule_030(single_space_between_tokens):
    '''
    Architecture rule 030 checks for a single space between the *architecture* keyword and the identifier.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'architecture', '030', token.architecture_keyword, token.identifier)
        self.solution = 'Reduce spaces between *architecture* keyword and identifier to a single space.'
