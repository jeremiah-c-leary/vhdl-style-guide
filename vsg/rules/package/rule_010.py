
from vsg.rules import case_rule
from vsg import check


class rule_010(case_rule):
    '''
    Package rule 010 checks the package name has proper case in the package declaration.
    '''

    def __init__(self):
        case_rule.__init__(self, 'package', '010', 'isPackageKeyword')
        self.solution = 'Change package name to '
        self.case = 'upper'

    def _extract(self, oLine):
        if not check.has_package_name(oLine):
            return []

        return [oLine.line.replace(';', '').split()[1]]
