
from vsg.rules import lower_case_rule


class rule_004(lower_case_rule):
    '''
    Component rule 004 checks the component keyword is lower case.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'component', '004', 'isComponentDeclaration', 'component')
        self.solution = 'Change "component" keyword to lowercase.'
