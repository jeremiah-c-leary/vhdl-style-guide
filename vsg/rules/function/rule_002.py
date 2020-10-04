
from vsg.rules import single_space_between_tokens

from vsg.token import function_specification as token


class rule_002(single_space_between_tokens):
    '''
    Entity rule 002 checks for a single space between the entity keyword and token identifier.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'function', '002', token.function_keyword, token.designator)
        self.solution = 'Reduce spaces between *function* keyword and designator to a single space.'
