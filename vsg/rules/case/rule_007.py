
from vsg.rules import previous_line

from vsg.token import case_statement as token


class rule_007(previous_line):
    '''
    Case rule 007 ensures a blank line exists before the "case" keyword.
    '''

    def __init__(self):
        previous_line.__init__(self, 'case', '007', [token.case_keyword])
        self.style = 'no_code'
