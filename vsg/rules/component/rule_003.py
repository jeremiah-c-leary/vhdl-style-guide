
from vsg.rules import previous_line

from vsg.token import component_declaration as token


class rule_003(previous_line):
    '''
    Component rule 003 checks for a blank line above the component keyword.
    '''

    def __init__(self):
        previous_line.__init__(self, 'component', '003', [token.component_keyword])
        self.style = 'no_code'
