
from vsg.rules import single_space_between_tokens

from vsg.token import procedure_specification as token


class rule_101(single_space_between_tokens):
    '''
    Procedure rule 101 checks there is a single space between the procedure name and the (.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'procedure', '101', token.designator, token.open_parenthesis)
        self.solution = 'Reduce spaces between designator and ( to a single space.'
