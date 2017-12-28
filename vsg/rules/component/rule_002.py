
from vsg.rules import single_space_after_rule


class rule_002(single_space_after_rule):
    '''
    Component rule 002 checks for a single space after the "component" keyword.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'component', '002', 'isComponentDeclaration', 'component')
        self.solution = 'Remove extra spaces after "component" keyword.'
