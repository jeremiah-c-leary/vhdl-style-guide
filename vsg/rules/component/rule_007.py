
from vsg.rules import single_space_between_tokens

from vsg.token import component_declaration as token


class rule_007(single_space_between_tokens):
    '''
    Component rule 007 checks for a single space before the "is" keyword.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'component', '007', token.identifier, token.is_keyword)
        self.solution = 'Reduce spaces between *component* keyword and identifier.'
