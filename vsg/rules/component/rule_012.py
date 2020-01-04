
from vsg.rules import case_rule
from vsg import utils


class rule_012(case_rule):
    '''
    Component rule 012 checks component name has proper case in "end" keyword line.
    '''

    def __init__(self):
        case_rule.__init__(self, 'component', '012', 'isComponentEnd')
        self.case = 'upper'
        self.solution = 'Change component name to '

    def _extract(self, oLine):
        return utils.extract_component_identifier(oLine)
