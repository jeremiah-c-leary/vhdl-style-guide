
from vsg.rules import case_rule
from vsg import utils


class rule_002(case_rule):
    '''
    Signal rule 002 checks the "signal" keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'signal', '002', 'isSignal')
        self.solution = 'Change "signal" keyword to '

    def _extract(self, oLine):
        return utils.extract_class_name(oLine)
