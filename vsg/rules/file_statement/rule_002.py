
from vsg.rules import lower_case_rule


class rule_002(lower_case_rule):
    '''
    File rule 002 checks the **file** keyword is lowercase.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'file', '002', 'isFileKeyword', 'file')
        self.solution = 'Change the "file" keyword to lowercase.'
