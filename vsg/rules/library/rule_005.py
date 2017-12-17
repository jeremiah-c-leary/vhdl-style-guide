
from vsg.rules import lower_case_rule


class rule_005(lower_case_rule):
    '''
    Library rule 005 checks the use keyword is lower case.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'library', '005', 'isLibraryUse', 'use')
        self.solution = 'Change "use" keyword to lowercase.'
