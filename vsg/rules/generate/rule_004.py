
from vsg.rules import previous_line

from vsg import token

lTokens = []
lTokens.append(token.case_generate_statement.generate_label)
lTokens.append(token.for_generate_statement.generate_label)
lTokens.append(token.if_generate_statement.generate_label)


class rule_004(previous_line):
    '''
    Ensures a blank line exists above the generate label.
    '''

    def __init__(self):
        previous_line.__init__(self, 'generate', '004', lTokens)
