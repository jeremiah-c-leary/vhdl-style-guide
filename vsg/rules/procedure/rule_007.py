
from vsg.rules import consistent_token_case

from vsg import token


class rule_007(consistent_token_case):
    '''
    Constant rule 007 checks case consistency of procedure names.
    '''

    def __init__(self):
        consistent_token_case.__init__(self, 'procedure', '007', [token.procedure_specification.designator])
