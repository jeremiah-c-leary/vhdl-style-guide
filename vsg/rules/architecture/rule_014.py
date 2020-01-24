
from vsg.rules import case_rule


class rule_014(case_rule):
    '''
    Architecture rule 014 checks the entity name has proper case in the architecture declaration.
    '''

    def __init__(self):
        case_rule.__init__(self, 'architecture', '014', 'isArchitectureKeyword')
        self.case = 'upper'
        self.solution = 'Change entity name to '

    def _extract(self, oLine):
        sLine = oLine.lineNoComment.split()
        if sLine[-1].lower() == 'is':
            return [sLine[-2]]

        return []
