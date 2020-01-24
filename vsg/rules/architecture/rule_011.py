

from vsg.rules import case_rule
from vsg import utils


class rule_011(case_rule):
    '''
    Architecture rule 011 checks the architecture name case on the closing "end architecture" line.
    '''

    def __init__(self):
        case_rule.__init__(self, 'architecture', '011', 'isEndArchitecture')
        self.case = 'upper'
        self.solution = 'Change architecture name to '

    def _extract(self, oLine):
        return utils.extract_architecture_identifier(oLine)
