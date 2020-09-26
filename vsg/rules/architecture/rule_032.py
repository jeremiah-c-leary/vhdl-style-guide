
from vsg.rules import single_space_between_tokens

from vsg.token import architecture_body as token

class rule_032(single_space_between_tokens):
    '''
    Architecture rule 032 checks for a single space between the *of* keyword and the entity_name.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'architecture', '032', token.of_keyword, token.entity_name)
        self.solution = 'Reduce spaces between *of* keyword and entity_name to a single space.'
