
from vsg.rules import case_rule
from vsg import utils


class rule_004(case_rule):
    '''
    Signal rule 004 checks the signal name has proper case.
    '''
    def __init__(self, name='signal', identifier='004'):
        case_rule.__init__(self, 'signal', '004', 'isSignal')
        self.solution = 'Change signal identifiers name to '

    def _extract(self, oLine):
        return utils.extract_class_identifier_list(oLine)
