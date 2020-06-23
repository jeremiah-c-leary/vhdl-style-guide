
from vsg.rules import case_rule
from vsg import utils


class rule_028(case_rule):
    '''
    Architecture rule 028 checks the "architecture" keyword in "end architecture" has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'architecture', '028', 'isEndArchitecture')
        self.solution = 'Change "architecture" keyword to '

    def _extract(self, oLine):
        return utils.extract_words(oLine, ['architecture'])
