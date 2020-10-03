
from vsg.rules import single_space_between_tokens

from vsg.token import entity_declaration as token


class rule_002(single_space_between_tokens):
    '''
    Entity rule 002 checks for a single space between the entity keyword and token identifier.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'entity', '002', token.entity_keyword, token.identifier)
        self.solution = 'Reduce spaces between *entity* keyword and identifier to a single space.'
