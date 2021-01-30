
from vsg.rules import previous_line

from vsg import token

lTokens = []
lTokens.append(token.process_statement.process_keyword)
lTokens.append(token.process_statement.process_label)


class rule_015(previous_line):
    '''
    Checks for a blank line above the "process" keyword.
    '''

    def __init__(self):
        previous_line.__init__(self, 'process', '015', lTokens)
        self.style = 'no_code'
