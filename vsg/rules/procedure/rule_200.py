
from vsg.rules import previous_line

from vsg import token

lTokens = []
lTokens.append(token.procedure_specification.procedure_keyword)


class rule_200(previous_line):
    '''
    Checks for a blank line above the procedure keyword.
    '''

    def __init__(self):
        previous_line.__init__(self, 'procedure', '200', lTokens)
