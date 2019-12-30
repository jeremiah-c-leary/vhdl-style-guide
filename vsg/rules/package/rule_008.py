
from vsg.rules import case_rule
from vsg import check


class rule_008(case_rule):
    '''
    Package rule 008 checks the package name has proper case on the closing "end package" line.
    '''

    def __init__(self):
        case_rule.__init__(self, 'package', '008', 'isPackageEnd')
        self.solution = 'Change package name to '
        self.case = 'upper'

    def _extract(self, oLine):
        if not check.has_package_name(oLine):
            return []

        return [oLine.line.replace(';', '').split()[-1]]
