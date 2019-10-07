
from vsg.rules import case_rule
from vsg import utils


class rule_008(case_rule):
    '''Component rule 008 checks the component name has proper case in the component declaration line.'''

    def __init__(self):
        case_rule.__init__(self, 'component', '008', 'isComponentDeclaration')
        self.case = 'upper'
        self.solution = 'Change component name to ' + self.case + 'case'

    def _extract(self, oLine):
        return utils.extract_component_identifier(oLine)
