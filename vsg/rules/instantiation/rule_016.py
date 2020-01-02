
from vsg.rules import case_rule


class rule_016(case_rule):
    '''
    Instantiation rule 016 checks the generic name has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'instantiation', '016', 'isInstantiationGenericAssignment')
        self.case = 'upper'
        self.solution = 'Change generic name to '

    def _extract(self, oLine):
        ret = []
        if not oLine.isInstantiationGenericKeyword:
            ret.append(oLine.line.split()[0])

        return ret
