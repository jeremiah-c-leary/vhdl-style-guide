
from vsg.rules import lower_case_rule


class rule_004(lower_case_rule):
    '''
    Library rule 004 checks the library keyword is lower case.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'library', '004', 'isLibrary', 'library')
        self.solution = 'Change "library" keyword to lowercase.'
