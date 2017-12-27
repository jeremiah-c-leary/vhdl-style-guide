
from vsg.rules.architecture import architecture_case_rule


class rule_014(architecture_case_rule):
    '''
    Architecture rule 014 checks the entity name is upper case in the architecture declaration.
    '''

    def __init__(self):
        architecture_case_rule.__init__(self, 'architecture', '014', 3)
        self.solution = 'Upper case entity name.'
