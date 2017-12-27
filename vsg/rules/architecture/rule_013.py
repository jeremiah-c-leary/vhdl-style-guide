
from vsg.rules.architecture import architecture_case_rule


class rule_013(architecture_case_rule):
    '''
    Architecture rule 013 checks the architecture name is upper case in the architecture declaration.
    '''

    def __init__(self):
        architecture_case_rule.__init__(self, 'architecture', '013', 1)
        self.solution = 'Upper case architecture name.'
