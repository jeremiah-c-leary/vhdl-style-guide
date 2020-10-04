
from vsg.rules import single_space_between_tokens

from vsg.token import function_specification as token


class rule_003(single_space_between_tokens):
    '''
    Function rule 003 checks there is a single space between the function name and the (.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'function', '003', token.designator, token.open_parenthesis)
        self.solution = 'Reduce spaces between *function* keyword and designator to a single space.'
