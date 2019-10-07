
from vsg.rules import case_rule
from vsg import utils


class rule_008(case_rule):
    '''
    Instantiation rule 008 checks the instance name has proper case in the instantiation declaration line.
    '''

    def __init__(self):
        case_rule.__init__(self, 'instantiation', '008', 'isInstantiationDeclaration', utils.extract_label)
        self.case = 'upper'
        self.solution = 'Change instance name to ' + self.case + 'case'
