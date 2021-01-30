
from vsg.rules import previous_line

from vsg.token import case_statement as token


class rule_009(previous_line):
    '''
    Case rule 009 ensures a blank line exists above the "end case" keywords.
    '''

    def __init__(self):
        previous_line.__init__(self, 'case', '009', [token.end_keyword])
