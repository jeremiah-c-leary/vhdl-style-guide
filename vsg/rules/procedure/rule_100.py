
from vsg.rules import single_space_between_tokens

from vsg.token import procedure_specification as token


class rule_100(single_space_between_tokens):
    '''
    Procedure rule 100 checks for a single space between the procedure keyword and procedure name.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'procedure', '100', token.procedure_keyword, token.designator)
        self.solution = 'Reduce spaces between *procedure* keyword and designator to a single space.'
