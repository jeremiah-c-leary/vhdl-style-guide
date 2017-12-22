
from vsg.rules import lower_case_rule


class rule_017(lower_case_rule):
    '''
    Port rule 017 checks the "port" keyword is lowercase.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'port', '017', 'isPortKeyword', 'port')
        self.solution = 'Change "port" keyword to lowercase.'
