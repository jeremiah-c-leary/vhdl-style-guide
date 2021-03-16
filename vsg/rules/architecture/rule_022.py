
from vsg.rules import single_space_between_tokens

from vsg.token import architecture_body as token

class rule_022(single_space_between_tokens):
    '''
    Architecture rule 022 checks for a single space between the *end* and *architecture* keywords.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'architecture', '022', token.end_architecture_keyword, token.architecture_simple_name)
        self.solution = 'Reduce spaces between *architecture* keyword and architecture_simple_name to a single space.'
