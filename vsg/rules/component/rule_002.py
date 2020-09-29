
from vsg.rules import single_space_between_tokens

from vsg.token import component_declaration as token


class rule_002(single_space_between_tokens):
    '''
    Component rule 002 checks for a single space between the "component" keyword and the identifier.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'component', '002', token.component_keyword, token.identifier)
        self.solution = 'Reduce spaces between *component* keyword and identifier.'
