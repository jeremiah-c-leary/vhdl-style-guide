
from vsg.rules import single_space_between_tokens

from vsg.token import architecture_body as token

class rule_012(single_space_between_tokens):
    '''
    Architecture rule 012 checks for a single space between the *end* and *architecture* keywords.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'architecture', '012', token.end_keyword, token.end_architecture_keyword)
        self.solution = 'Reduce spaces between *end* and *architecture* keywords to a single space.'
