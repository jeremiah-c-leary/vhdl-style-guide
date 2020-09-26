
from vsg.rules import single_space_between_tokens

from vsg.token import architecture_body as token

class rule_031(single_space_between_tokens):
    '''
    Architecture rule 031 checks for a single space between the *architecture* keyword and the identifier.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'architecture', '031', token.identifier, token.of_keyword)
        self.solution = 'Reduce spaces between identifier and *of* keyword to a single space.'
