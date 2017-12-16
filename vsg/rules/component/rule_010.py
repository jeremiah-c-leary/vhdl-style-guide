
from vsg.rules import lower_case_rule


class rule_010(lower_case_rule):
    '''
    Component rule 010 checks the "end" keyword is lowercase.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'component', '010', 'isComponentEnd', 'end')
        self.solution = 'Change "end" keyword to lowercase.'
